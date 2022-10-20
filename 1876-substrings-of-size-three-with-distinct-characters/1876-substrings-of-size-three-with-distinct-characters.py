class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        if len(s) < 3:
            return 0
        res = 0
        sub = s[:3]
        if len(set(sub)) == 3:
            res += 1
        l = 0
        for r in range(3, len(s)):
            sub = s[l+1:r+1]
            
            if len(set(sub)) == 3:
                res += 1
            l += 1
        return res