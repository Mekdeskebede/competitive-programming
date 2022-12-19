class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)
        visited = set()
        def dfs(node):
            if node == destination: 
                return True
            if node not in visited:
                visited.add(node)
                for edge in graph[node]:
                    res = dfs(edge)
                    if res: 
                        return True
        return dfs(source)