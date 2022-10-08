class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        no_sol = math.inf
        min_sub = no_sol
        left ,right = 0, 0
        temp_sum = 0
        while left < len(nums):
            
            temp_sum += nums[left]
            
            if temp_sum >= target:
                while temp_sum >= target:
                    min_sub = min(min_sub, left - right + 1)
                    temp_sum -= nums[right]
                    right += 1
            left += 1
            
        return 0 if min_sub == no_sol else min_sub
            
            
        