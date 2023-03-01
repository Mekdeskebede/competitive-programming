class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        if n == 1 or n == k:
            return n
        
        longest = 0
        max_len = 0
        string = defaultdict(int)
        left = 0
        
        for right in range(n):
            string[s[right]] += 1
            longest = max(longest,string[s[right]])
            
            while (right-left) - longest >= k:
                string[s[left]] -= 1
                if string[s[left]] == 0:
                    del string[s[left]]
                left += 1
                
            max_len = max(max_len, right-left+1)
        
        return max_len
            