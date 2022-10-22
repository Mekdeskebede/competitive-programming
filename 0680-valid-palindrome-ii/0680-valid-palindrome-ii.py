class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                p1 = s[l+1:r+1]
                p2 = s[l:r]
                
                return True if p1 == p1[::-1] or p2 == p2[::-1] else False
                
        return True
                