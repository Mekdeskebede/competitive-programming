from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.representative = {i:i for i in range(n+1)}
        self.rank = [1] * (n+1)
        self.maximum = 1
        self.connection = {i:1 for i in range(n+1)}
    def find(self, x):
        if self.representative[x] != x:
            self.representative[x] = self.find(self.representative[x])
        return self.representative[x]
    def union(self, x, y):
    
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            if self.rank[rep_x] > self.rank[rep_y]:
                rep_x, rep_y = rep_y, rep_x
                
            self.rank[rep_y] += self.rank[rep_x]
            self.representative[rep_x] = rep_y
            self.maximum = max(self.maximum, self.rank[rep_y],self.rank[rep_x])
        # self.connection[x] += self.connection[y] 
        # self.connection[y] += self.connection[x] 
        # self.maximum = max(self.maximum, self.connection[x], self.connection[y])
 
n, d = map(int,input().split())
uf = UnionFind(n)
for i in range(d):
    start, end = map(int, input().split())
    uf.union(start,end)
    print(uf.maximum-1)
    # print(uf.representative)
