from collections import defaultdict, deque

def bfs(graph, sequence):
    queue = deque()
    queue.append(1)
    visited = set()
    idx = 0
    while queue:
        order = []
        level = len(queue)
        for i in range(level):
            cur = queue.popleft()
            order.append(cur)
            visited.add(cur)
            for elem in graph[cur]:
                if elem not in visited:
                    queue.append(elem)
        if sorted(order) != sorted(sequence[idx:idx + len(order)]):
            return "No"
        
        idx += len(order)
    return "Yes"
n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
   a, b = list(map(int, input().split()))
   graph[a].append(b)
   graph[b].append(a)

sequence = list(map(int, input().split()))
print(bfs(graph, sequence))

