class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # for i in range(len(nums)):
        pointer = 0
        while pointer < len(nums):
            if nums[pointer] == val:
                nums.pop(pointer)
            else:
                pointer += 1
        return len(nums)