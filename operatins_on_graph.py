from collections import defaultdict

vertices = int(input())
graph = defaultdict(list)
k = int(input())

for _ in range(k):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        graph[operation[1]].append(operation[2])
        graph[operation[2]].append(operation[1])
    else:
        print(*graph[operation[1]])

