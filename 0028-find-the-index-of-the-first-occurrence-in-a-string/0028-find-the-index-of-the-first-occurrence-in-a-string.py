class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n_hash = 0
        curr_hash = 0
        n = len(haystack)
        m = len(needle)
        if m > n:
            return -1
        a = 27
        for i in range(m):
            n_hash += (a**(m-i-1) * (ord(needle[i])-96))
            curr_hash += (a**(m-i-1) * (ord(haystack[i])-96))
            
        if curr_hash == n_hash:
            return 0
        left = 0
        for right in range(m,n):
            curr_hash -= ((ord(haystack[left])-96)*(a**(m-1)))
            left += 1
            curr_hash *= a
            curr_hash += (ord(haystack[right])-96)
            if curr_hash == n_hash:
                return left
            
        return -1
        