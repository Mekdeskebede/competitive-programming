class Solution:
    def __init__(self):
        self.representative =  defaultdict(str)
        
    def find(self,char):
        while char != self.representative[char]:
            char = self.representative[char]
        return self.representative[char]
    
    def union(self, char1, char2):
        
        if char1 not in self.representative:
            self.representative[char1] = char1
        if char2 not in self.representative:
            self.representative[char2] = char2
        rep1 = self.find(char1)
        rep2 = self.find(char2)
            
        if rep1 > rep2:
            self.representative[rep1] = rep2
        else:
            self.representative[rep2] = rep1
            
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        for i in range(len(s1)):
            self.union(s1[i],s2[i])
        ans = []
        for char in baseStr:
            if char in self.representative:
                ans.append(self.find(char))
            else:
                ans.append(char)
                
        return "".join(ans)
        