class UnionFind:
    def __init__(self):
        self.representative = {}
        self.rank = {}
        
    def find(self, x):
        if x not in self.representative:
            self.representative[x] = x
            self.rank[x] = 1
            return x
        while self.representative[x] != x:
            x = self.representative[x]
        return x
    
    def union(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            if self.rank[rep_x] > self.rank[rep_y]:
                rep_x, rep_y = rep_y, rep_x
                
            self.representative[rep_x] = rep_y
            self.rank[rep_y] += self.rank[rep_x]
            
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        owner = {}
        uf = UnionFind()
        
        for acc in accounts:
            parent = acc[0]
            rep = uf.find(acc[1])
            for i in range(2,len(acc)):
                child = uf.find(acc[i])
                uf.union(rep, child)
            owner[uf.find(rep)] = parent
            
        groups = defaultdict(list)
        for key, val in uf.representative.items():
            groups[uf.find(val)].append(key)
            
        for key in groups:
            groups[key].sort()
            
        ans = []
        for key in groups:
            temp = []
            temp.append(owner[key])
            for email in groups[key]:
                temp.append(email)
            ans.append(temp)
                      
        return ans
                