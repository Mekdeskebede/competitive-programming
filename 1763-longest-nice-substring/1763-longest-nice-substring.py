class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        res = ""
        
        for l , val in enumerate(s):
            r = l + 1
            sub = val
            while r < len(s):
                sub += s[r]
                if len(set(sub.lower())) == len(set(sub))/2:
                    res = max(res, sub, key = len)
                r += 1
        return res
