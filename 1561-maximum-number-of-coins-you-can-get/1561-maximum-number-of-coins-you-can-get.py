class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        left = 0
        right = len(piles)-1
        me = 0
        piles.sort()
        while left < right:
            right -= 1
            if left <= right:
                me += piles[right]
                right -= 1
            if left < right:
                left += 1
        return me
        
        
        