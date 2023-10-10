class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        
        for i,(s,e) in enumerate(equations):
            adj_list[s].append([values[i],e])
            adj_list[e].append([(1/values[i]),s])
            
        def dfs(node,curr,target):
            if node not in adj_list or target not in adj_list:
                return -1
            if node in adj_list and target in adj_list and node == target:
                return curr
            visited.add(node)
            for (val,neighbor) in adj_list[node]:
                if neighbor not in visited:
                    ans = dfs(neighbor,curr*val,target) 
                    if ans != -1:
                        return ans
                    
            return -1
        
        ans = []
        for a,b in queries:
            visited = set()
            ans.append(dfs(a,1,b))
            
        return ans
        