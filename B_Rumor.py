from collections import defaultdict, deque
import sys
def solution():
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    adj_list = defaultdict(list)

    for i in range(m):
        edge = list(map(int,input().split()))
        adj_list[edge[0]-1].append(edge[1]-1)
        adj_list[edge[1]-1].append(edge[0]-1)

    visited = set()
    queue = deque()
    minimum = float('inf')
    def bfs():
        nonlocal minimum
        while queue:
            node = queue.popleft()
            minimum = min(minimum, arr[node])
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    minimum = min(minimum, arr[neighbor])
                    queue.append(neighbor)
                    visited.add(neighbor)
    
    group = 0
    for i in range(n):
        minimum = float('inf')
        if i not in adj_list:
            group += arr[i]
        elif arr[i] not in visited:
            queue = deque([i])
            visited.add(i)
            bfs()
            group += minimum

    print(group)

solution()

# from collections import defaultdict

# n, m = map(int,input().split())
# arr = list(map(int,input().split()))
# adj_list = defaultdict(list)

# for i in range(m):
#     edge = list(map(int,input().split()))
#     adj_list[edge[0]-1].append(edge[1]-1)
#     adj_list[edge[1]-1].append(edge[0]-1)

# visited = set()
# def dfs(city):
#     visited.add(city)
#     for neighbor in adj_list[city]:
#         if neighbor not in visited:
#             dfs(neighbor)

# arr.sort()
# group = 0
# for i in range(len(arr)):
#     if arr[i] not in adj_list:
#         group += arr[i]
#     elif arr[i] not in visited:
#         group += arr[i]
#         dfs(arr[i])

# print(group)









