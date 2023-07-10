class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        adj_list = defaultdict(list)
        for i in range(1,len(parent)):
            adj_list[parent[i]].append(i)
            adj_list[i].append(parent[i])
        
        @cache
        def dfs(node, parent):
            length = 1
            for neighbor in adj_list[node]:
                if neighbor == parent: continue
                if s[neighbor] != s[node]:
                    length = max(length, dfs(neighbor, node) + 1)
            return length
        return max(dfs(i, -1) for i in range(len(parent)))
            
            
            
            
            
            