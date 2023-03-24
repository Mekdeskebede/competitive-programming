class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            while i + 1 != nums[i]:
                temp = nums[i]-1
                if nums[i] == nums[temp]:
                    return nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]