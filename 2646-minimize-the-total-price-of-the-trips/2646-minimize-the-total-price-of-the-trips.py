class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        count = [0] * n
        def dfs1(node,end,parent):

            if end == node:
                return True 
            for child in adj_list[node]:
                if child != parent:
                    if dfs1(child,end,node):
                        count[child] += 1
                        return True
            return False
                
        adj_list = defaultdict(list)
        for s,e in edges:
            adj_list[e].append(s)
            adj_list[s].append(e)
        
        for x,y in trips:
            count[x] += 1
            dfs1(x,y,-1)
            
        for i in range(n):
            price[i] *= count[i]
       
        def dfs2(node,par):
            half = price[node]//2
            non_half = price[node]
            for i in adj_list[node]:
                if i != par:
                    hlf,nhlf=dfs2(i,node)
                    half+=nhlf
       
                    non_half=min(non_half+hlf,non_half+nhlf)
            return (half,non_half)
        
        return min(dfs2(0,-1))
        