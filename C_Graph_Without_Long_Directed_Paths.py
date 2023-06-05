from collections import defaultdict, deque

adj_list = defaultdict(list)

n, m = map(int, input().split())
edges = []

for i in range(m):
    start, end = map(int, input().split())
    edges.append((start-1,end-1))
    adj_list[start-1].append(end-1)
    adj_list[end-1].append(start-1)

def bfs():
    color = [-1] * n
    queue = deque([0])
    color[0] = 0
    visited = set([0])
    ans = []

    while queue:
        node = queue.popleft()
        for neighbor in adj_list[node]:
            if color[neighbor] == color[node]:
                return "NO"
            

            if neighbor not in visited:
                
                color[neighbor] = 1 - color[node]
                visited.add(neighbor)
                queue.append(neighbor)
                
    for start, end in edges:
        if color[start] == 1:
            ans.append("0")
        else:
            ans.append("1")

    return "YES \n" + "".join(ans)

print(bfs())

                



