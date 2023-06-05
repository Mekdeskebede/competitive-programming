from collections import defaultdict

n = int(input())
adj_list = defaultdict(list)

for i in range(n):
    edge = list(map(int,input().split()))
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])
visited = set()
ans =[]
def dfs(node):
    visited.add(node)
    ans.append(node)
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            dfs(neighbor)

for key in adj_list:
    if len(adj_list[key]) <= 1:
        dfs(key)
        break
print(*ans)