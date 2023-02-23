class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        n = len(nums)
        arr_sum =0
        min_sub = float("inf")
        
        left = 0
        for right in range(0,n):
            arr_sum += nums[right]
            
            while arr_sum >= target and left <= right:
                
                min_sub = min(min_sub, right-left+1)
                arr_sum -= nums[left]
                left += 1
                
        return 0 if min_sub == float("inf") else min_sub
        
        

      