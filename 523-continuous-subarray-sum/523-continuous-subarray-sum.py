class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # pre_sum = []
        sum = 0
        remainder = {0 : -1}
        for idx, val in enumerate(nums):
            sum += val
            mod = sum % k
            if mod in remainder and idx - remainder[mod] >= 2:
                return True
            elif mod not in remainder:
                remainder[mod] = idx
        return False
            
        
        