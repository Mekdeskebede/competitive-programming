class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def countDivisor(divisor):
            res = 0
            for num in nums:
                if num % divisor == 0:
                    res += num // divisor
                else:
                    res += num // divisor + 1
            return res
            
        low = 1
        high = max(nums)
        
        while low <= high:
            mid = low + (high - low)//2
            
            if countDivisor(mid) > threshold:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
        