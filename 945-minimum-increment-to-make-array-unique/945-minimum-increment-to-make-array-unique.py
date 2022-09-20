class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count, prev = 0 , nums[0]
        
        for i in range(1, n):
            if nums[i] <= prev:
                count = count + prev + 1 - nums[i]
                nums[i] = prev + 1          
            prev = nums[i]
        return count