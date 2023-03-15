class Solution:
    def balancedString(self, s: str) -> int:
        
        n = len(s)
        count = {"Q":0, "W":0, "E":0, "R":0}
        for char in s:
            count[char] += 1
        
        balanced = n//4
        min_len = float("inf")
        replace = {}
        
        for key, val in count.items():
            if val > balanced:
                replace[key] = val - balanced
        
        unique = len(replace)
        if unique == 0:
            return 0 
        left = 0
        
        for right in range(n):
            if s[right] in replace:
                replace[s[right]] -= 1
                if replace[s[right]] == 0:
                    unique -= 1
                    
            while unique == 0:
                min_len = min(min_len,right-left+1)
                if s[left] in replace:
                    replace[s[left]] += 1
                    if replace[s[left]] == 1:
                        unique += 1
                left += 1
                
        return min_len
            