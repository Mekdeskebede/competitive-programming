class UnionFind:
    def __init__(self, size):
        self.representative = {i:i for i in range(1, size+1)}
        self.rank = [1] * (size+1)
    
    def find(self, x):
        while x != self.representative[x]:
            x = self.representative[x]
        return x
    
    def union(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)
        if xrep == yrep:
            return True
        if self.rank[xrep] > self.rank[yrep]:
            xrep, yrep = yrep, xrep
        self.representative[yrep] = self.representative[xrep]
        self.rank[xrep] += self.rank[yrep]
        return False
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for start, end in edges:
            cycle = uf.union(start, end)
            if cycle:
                return [start, end]
        return []