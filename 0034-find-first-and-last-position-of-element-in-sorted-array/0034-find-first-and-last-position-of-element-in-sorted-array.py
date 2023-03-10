class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left)//2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low)//2
            
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
                
        if left > high:
            return [-1,-1]
        else:
            return [left,high]
                