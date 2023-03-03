class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def countK(k):
            hour = 0
            for pile in piles:
                if pile%k==0:
                    hour += pile//k
                else:
                    hour += pile//k + 1
            return hour
        
        low = 1
        high = max(piles)
        
        while low <= high:
            mid = low + (high-low)//2
            if countK(mid) > h:
                low = mid + 1
            else:
                high = mid - 1
                
        return low