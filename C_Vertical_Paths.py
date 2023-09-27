from collections import defaultdict


def dfs(node):
    for neighbour in adj_list[node]:
        visited.add(node)
        curr.append(node)
        
        if node not in adj_list:
            return
        if neighbour not in visited:
            dfs(neighbour)

test = int(input())

for _ in range(test):
    n = int(input())
    parents = list(map(int,input().split()))
    adj_list = defaultdict(list)
    for i in range(n):
        if i+1 == parents[i]:
            initial = i+1
        else:
            adj_list[parents[i]].append(i+1)
    print(adj_list)

    visited = set()
    curr = []
    dfs(initial)
    if curr:
        print(len(curr))
        print(*curr)
    for key in adj_list:
        curr = []
        if key not in visited:
            dfs(key) 
        if curr:
            print(len(curr))
            print(*curr)
    for i in range(1,n+1):
        curr = []
        if i not in visited:
            dfs(i) 
        if curr:
            print(len(curr))
            print(*curr)

    
