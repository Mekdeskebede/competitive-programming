class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        
        
        pre_sum = 0
        for i in range(len(nums)):

            pre_sum += nums[i]
            nums[i] = pre_sum
            
        return nums