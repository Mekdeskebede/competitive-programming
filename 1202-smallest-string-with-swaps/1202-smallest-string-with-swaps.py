class UnionFind:
    def __init__(self,s):
        self.representative = {i:i for i in range(len(s))}
        self.rank = [1] * len(s)
        self.s = s
        
    def find(self, x):
        if self.representative[x] != x:
            self.representative[x] = self.find(self.representative[x])
        return self.representative[x]
    
    def union(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            if self.rank[rep_x] > self.rank[rep_y]:
                rep_x, rep_y = rep_y, rep_x
                
            self.representative[rep_x] = rep_y
            self.rank[rep_y] += self.rank[rep_x]

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(s)
        for start, end in pairs:
            uf.union(start, end)
        
        groups = defaultdict(list)
        for key in uf.representative:
            keyNew = uf.find(key)
            groups[uf.representative[keyNew]].append(s[key])
            
        for key in groups:
            groups[key].sort()
            
        pointers = {}
        for key in groups:
            pointers[key] = 0
            
        ans = []
        for i in range(len(s)):
            rep = uf.find(i)
            ans.append(groups[rep][pointers[rep]])
            pointers[rep] += 1
        
        return "".join(ans)