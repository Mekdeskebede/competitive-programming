class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        zero = 0 
        one = 0
        res = 0
        
        for i in range(len(s)):
            if s[i] == "0":
                zero = 1 if i > 1 and s[i] != s[i-1] else zero + 1
                if zero <= one:
                    res += 1
            else:
                one = 1 if i > 1 and s[i] != s[i-1] else one + 1
                if zero >= one:
                    res += 1
        return res