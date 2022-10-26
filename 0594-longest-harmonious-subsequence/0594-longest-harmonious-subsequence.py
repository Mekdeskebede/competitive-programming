class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        l = 0
        r = 1
        res = 0
        while r < len(nums):
            if l < len(nums) and nums[r] - nums[l] == 1:
                res = max(res, r - l + 1)
                r += 1
            elif nums[r] - nums[l] < 1:
                r += 1
            else:
                l += 1
        return res
            