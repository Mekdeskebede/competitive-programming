class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(s, prev):

            if int(s) == int(prev) - 1: return True

            for i in range(1, len(s)+1):
                
                if int(s[:i]) == int(prev) - 1 and backtrack(s[i:], s[:i]): return True
                
            return False
        
        for i in range(1, len(s)):
            if backtrack(s[i:], s[:i]): return True

        return False
    
