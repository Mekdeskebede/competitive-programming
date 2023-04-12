class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        adj_list = defaultdict(list)
                
        final_paths = []
        
        def dfs(idx,path):
            path.append(idx)
            if idx == len(graph) -1:
                final_paths.append(path[:])
                
            for adj in graph[idx]:
                dfs(adj,path)
                path.pop()
                
        dfs(0,[])
        return final_paths
       
        