class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = float("-inf")
        
        pre_sum = 0
        
        for i in range(len(nums)):
            pre_sum += nums[i]
            ans = max(ans, math.ceil(pre_sum/(i+1)))
            
        return ans