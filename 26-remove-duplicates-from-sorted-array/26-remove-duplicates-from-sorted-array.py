class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        pointer = 0
        while pointer < len(nums):
            temp = pointer + 1
            while temp < len(nums)-1 and nums[pointer] == nums[temp]:
                nums.pop(temp)
            pointer = temp
        if len(nums) >= 2 and nums[-1] == nums[-2]:
            nums.pop()
        return len(nums)
                