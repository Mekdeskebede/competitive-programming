class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        adj_list = defaultdict(list)
        visited = set()

        self.ans = 0
        
        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)

        visited = set()
        def dfs(node):
            
            visited.add(node)
            if len(adj_list[node]) == 1 and node!= 0:
                if hasApple[node]:
                    return 2
                return 0
            
            total = 0
            for neighbor in adj_list[node]:
                if neighbor in visited:
                    continue                
                total += dfs(neighbor) 

            if (total or hasApple[node]) and node!= 0:
                return total + 2
            return total
                    
        return dfs(0)
        # return self.ans