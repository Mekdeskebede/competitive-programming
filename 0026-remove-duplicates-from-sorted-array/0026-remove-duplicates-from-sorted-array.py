class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        left = 0
        
        while left < len(nums):
            
            right = left + 1
            while right < len(nums) and nums[left] == nums[right]:
                nums.pop(right)
                
            left += 1
            
        return len(nums)