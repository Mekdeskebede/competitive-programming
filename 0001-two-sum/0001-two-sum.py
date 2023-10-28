class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            nums[i] = [nums[i],i]
        nums.sort()
        left = 0
        right = len(nums) - 1
        
        while left < right:
            curr = nums[left][0] + nums[right][0]
            if curr ==  target:
                return [nums[left][1],nums[right][1]]
            if curr > target:
                right -= 1
            else:
                left += 1
        