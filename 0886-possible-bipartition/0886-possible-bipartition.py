class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        for u, v in dislikes:
            adj_list[u - 1].append(v - 1)
            adj_list[v - 1].append(u - 1)
        
        colors = [-1] * n
        
        for vertex in range(n):
            
            if colors[vertex] == -1:
                
                queue = collections.deque([vertex])
                colors[vertex] = 1
                
                while queue:
                    v = queue.popleft()
                    for neighbor in adj_list[v]:
                        if colors[neighbor] == -1:
                            
                            colors[neighbor] = 1 - colors[v]
                            queue.append(neighbor)
                            
                        elif colors[neighbor] == colors[v]:
                            return False
        return True