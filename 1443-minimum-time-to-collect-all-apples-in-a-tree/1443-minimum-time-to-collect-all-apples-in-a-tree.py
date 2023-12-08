class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        adj_list = defaultdict(list)
        visited = set()
        
        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)
            
        def dfs(node):
            visited.add(node)
            if not adj_list[node]:
                return 0
            temp = 0
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    
                    temp += dfs(neighbor)
                    
            if( hasApple[node] or temp ) and node != 0:
                return temp + 2
            
            return temp
        
        return dfs(0)