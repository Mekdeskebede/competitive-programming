class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
         
        freq = defaultdict(int)
        for x in range(lowLimit, highLimit+1):
            freq[sum(int(xx) for xx in str(x))] += 1
            
        return max(freq.values())