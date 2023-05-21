class Solution:
    
    def __init__(self):
        self.representative = {}
        self.rank = {}
    def find(self,x):
        if x not in self.representative:
            self.representative[x] = x
            return x
        while x != self.representative[x]:
            x = self.representative[x]
        return x
    def union(self, x, y):
        if x not in self.representative:
            self.representative[x] = x
            self.rank[x] = 1
        if y not in self.representative:
            self.representative[y] = y
            self.rank[y] = 1
            
        xrep = self.find(x)
        yrep = self.find(y)
        if self.rank[xrep] > self.rank[yrep]:
            xrep, yrep = xrep, yrep
        self.representative[xrep] = yrep
        self.rank[yrep] += self.rank[xrep]
        
    def equationsPossible(self, equations: List[str]) -> bool:
        for equ in equations:
            if equ[1] == '=':
                self.union(equ[0],equ[-1])
        for equ in equations:
            if equ[1] == '!':
                if self.find(equ[0]) == self.find(equ[-1]):
                    return False
        return True