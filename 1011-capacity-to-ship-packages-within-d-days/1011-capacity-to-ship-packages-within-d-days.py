class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def countDays(weight):
            d = 1
            count = 0
            
            for weight in weights:
                count += weight
                if count > mid:
                    d += 1
                    count = weight
            return d
        
        low = max(weights)
        high = sum(weights)
        
        while low <= high:
            
            mid = low + (high-low)//2
            if countDays(mid) > days:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
            
                