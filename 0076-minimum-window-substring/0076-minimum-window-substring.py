class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        n = len(s)
        t_count = Counter(t)
        left = 0
        count = len(t_count)
        window = " " * n 
        
        for right in range(n):
            
            if s[right] in t_count:
                t_count[s[right]] -= 1
                if t_count[s[right]] == 0:
                    count -= 1
                    
            while count == 0:
                if len(window) >= right - left + 1:
                    window = s[left:right+1]
                if s[left] in t_count:
                    t_count[s[left]] += 1
                    if t_count[s[left]] > 0:
                        count += 1
                left += 1
                
        return "" if window == (" " * n) else window