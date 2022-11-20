class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        h = len(nums) - 1
        
        left = -1
        while l <= h:
            mid = l + (h-l)//2
            if nums[mid] == target:
                left = mid
            if nums[mid] >= target:
                h = mid - 1
            else:
                l = mid + 1
        if left == -1:
            return [-1,-1]
        right = -1
        l = 0
        h = len(nums)-1
        while l <= h:
            mid = l + (h-l)//2
            if nums[mid] == target:
                right = mid
            if nums[mid] <= target:
                l = mid + 1
            else:
                h = mid - 1
        return [left, right]
        
                
        