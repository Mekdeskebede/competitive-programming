class Solution:
    def removePalindromeSub(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return 2
            else:
                l += 1
                r -= 1
        
        return 1