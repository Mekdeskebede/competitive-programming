class UnionFind:
    
    def __init__(self,size):
        self.representative = {i:i for i in range(1,size+1)}
        self.rank = [1] * (size + 1)
        self.minimum = [float("inf")] * (size + 1)
        
    def find(self,x):
        parent = self.representative[x]
        if x != parent:
            updated_parent = self.find(parent)
            self.representative[x] = updated_parent
        return self.representative[x]
    
    def union(self,x,y,weight):
        xrep = self.find(x)
        yrep = self.find(y)
        
        if self.rank[xrep] > self.rank[yrep]:
            xrep, yrep = yrep, xrep
        self.representative[yrep] = xrep
        self.rank[yrep] += self.rank[xrep]
        self.minimum[xrep] = min(self.minimum[yrep], self.minimum[xrep],weight)
            
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y, dist in roads:
            uf.union(x,y,dist)
            
        return uf.minimum[uf.find(1)]
            