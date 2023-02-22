class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        longest = 0
        
        if n == 0 or n == 1:
            return n
        
        left = 0
        right = 1
        unique = {s[left]:1}
        
        while right < n:
            
            unique[s[right]] = 1 + unique.get(s[right],0)
            
            while len(unique) < right - left + 1 and left <= right:
                
                unique[s[left]] -= 1
                if unique[s[left]] == 0:
                    del unique[s[left]]
                    
                left += 1 
                
            longest = max(longest,right - left + 1)
            right += 1
    
        return longest
            
            