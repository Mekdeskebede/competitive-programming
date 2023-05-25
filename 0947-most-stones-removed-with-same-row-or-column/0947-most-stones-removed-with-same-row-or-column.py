class UnionFind:
    def __init__(self,n):
        self.representative = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        
    def find(self, node):
        
        if node != self.representative[node]:
            self.representative[node] = self.find(self.representative[node])
        return self.representative[node]
    
    def union(self, x, y):

        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            if self.rank[rep_x] > self.rank[rep_y]:
                rep_x, rep_y = rep_y, rep_x

            self.rank[rep_y] += self.rank[rep_x]
            self.representative[rep_x] = rep_y

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind(len(stones))
        count = 0
        for i in range(len(stones)):
            for j in range(len(stones)):
                x1, y1= stones[i]
                x2, y2= stones[j]
                if x1 == x2 or y1 == y2:
                    uf.union(i, j)
                               
        for node, prnt in enumerate(uf.representative):
            if node == prnt:
                count += 1
        
        return len(uf.representative) - count