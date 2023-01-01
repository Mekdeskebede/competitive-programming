class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        pattern = list(pattern)
        s = s.split(' ')
        n = len(s)
        m = len(pattern)
        
        if m != n:
            return False
        
        p_s = {}
        s_p = {}
        
        for i in range(n):
            if pattern[i] in p_s and p_s[pattern[i]] != s[i]:
                return False
            p_s[pattern[i]] = s[i]
            
            if s[i] in s_p and s_p[s[i]] != pattern[i]:
                return False
            s_p[s[i]] = pattern[i]
        return True
        
        
        