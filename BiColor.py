from collections import defaultdict, deque
def bfs(adj_list,colors,n):

    for vertice in range(n):
        if colors[vertice] == -1:
            colors[vertice] = 1
            queue = deque([vertice])
            while queue:
                node = queue.popleft()
                for neighbor in adj_list[node]:
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1-colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    edges = int(input())
    adj_list = defaultdict(list)
    colors = [-1] * n
    for i in range(edges):
        s,e= map(int,input().split())
        adj_list[s-1].append(e-1)
        adj_list[e-1].append(s-1)
    if bfs(adj_list,colors,n):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")