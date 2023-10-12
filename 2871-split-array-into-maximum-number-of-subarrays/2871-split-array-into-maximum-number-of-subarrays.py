class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        curr_and = nums[0]
        for i in range(1,len(nums)):
            curr_and &= nums[i]
        
        if curr_and > 0:
            return 1
        
        ans = 0
        max_ = 2**32-1

        for n in nums:
            max_ &= n
            if max_ == 0:
                ans += 1
                max_ = 2**32-1

        return ans