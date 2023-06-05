from collections import defaultdict

n = int(input())
adj_list = defaultdict(list)
for _ in range(n):
    chain = input().split(' ')
    adj_list[chain[2].upper()].append(chain[0].upper())
def soln():
    max_depth = 0
    visited = set()
    def dfs(node,count):
        nonlocal max_depth
        max_depth = max(max_depth,count)
        for neighbour in adj_list[node]:
            dfs(neighbour,count+1)
    dfs('POLYCARP',1)
    print(max_depth)
soln()


