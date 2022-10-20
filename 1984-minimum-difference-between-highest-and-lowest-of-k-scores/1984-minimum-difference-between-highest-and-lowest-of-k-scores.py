class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums) < 2:
            return 0
        
        diff = nums[k-1] - nums[0]
        res = diff
        l = 1
        for r in range(k, len(nums)):
            diff = nums[r] - nums[l]
            res = min(res, diff)
            l += 1
        return res
            
            