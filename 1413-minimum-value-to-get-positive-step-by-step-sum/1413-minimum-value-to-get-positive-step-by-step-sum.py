class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i != 0:
                nums[i] += nums[i-1]
        ans = min(nums)
        
        if ans < 0:
            return abs(ans) + 1
        else:
            return 1