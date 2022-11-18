class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums)
        
        while l < r:
            mid = l + (r-l) // 2
            
            if mid == nums[mid]:
                l = mid + 1
            else:
                r = mid
        return l
        
        
        
        