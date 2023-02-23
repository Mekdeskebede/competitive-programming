class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        prefix = []
        
        pre_sum = 0
        for num in nums:
            
            pre_sum += num
            prefix.append(pre_sum)
            
        return prefix