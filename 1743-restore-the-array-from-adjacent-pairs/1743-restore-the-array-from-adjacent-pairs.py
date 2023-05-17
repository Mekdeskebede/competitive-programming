class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        adj_list = defaultdict(list)
        for start, end in adjacentPairs:
            adj_list[start].append(end)
            adj_list[end].append(start)
            
        for key in adj_list:
            if len(adj_list[key]) == 1:
                node = key
                break
        
        def dfs(node):
            ans.append(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        print(node)       
        ans = []
        visited = set([node])
        dfs(node)
        return ans
            