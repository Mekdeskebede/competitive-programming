class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        if n == 1 or n == k:
            return n
        
        longest = 0
        max_len = 0
        string = defaultdict(int)
         
        # print(string)
        for right in range(n):
            string[s[right]] += 1
            longest = max(longest,string[s[right]])
            print(string)
            
            if max_len - longest >= k:
                string[s[right - max_len]] -= 1
                # continue
            else:
                max_len += 1
            

        
        return max_len
            