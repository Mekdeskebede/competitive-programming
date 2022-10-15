class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        
        for i in range(len(t)):
            if i < len(s) and t[i] != s[i]:
                return t[i]
            elif i >= len(s):
                return t[i]
            
            
            