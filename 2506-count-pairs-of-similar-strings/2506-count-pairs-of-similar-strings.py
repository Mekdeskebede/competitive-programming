class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        count = {}
        for i in words:
            i = sorted(i)
            i = set(i)
            i = ''.join(i)
            count[i] = 1 + count.get(i, 0)
        ans = 0
        
        for key, val in count.items():
            if val > 1:
                ans += ((val * (val+ 1))/2)-val
        return int(ans)
                
            