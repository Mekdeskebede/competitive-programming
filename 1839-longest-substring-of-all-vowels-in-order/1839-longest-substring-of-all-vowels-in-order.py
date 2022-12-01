class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        visited = set()
        l = 0
        res  = 0
        
        for r in range(len(word)):
            if word[r-1] > word[r]:
                l = r
                visited = set()

            visited.add(word[r])
            
            if len(visited) > 4:
                res = max(res, r - l + 1)  
                
        return res