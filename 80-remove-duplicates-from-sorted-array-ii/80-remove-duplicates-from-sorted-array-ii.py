class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        while left < len(nums):
            right = left
            while right < len(nums) and nums[left] == nums[right]:
                if right - left >= 2:
                    nums.pop(right)
                else:
                    right += 1
            left = right
            
        return len(nums)
                    
        