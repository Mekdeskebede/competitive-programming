class Solution:
    def minOperations(self, nums: List[int]) -> int:
        step = 0
        count = Counter(nums)
        
        for key in count:
            if count[key]  == 1:
                return -1
            step += ceil(count[key]/3)
                
        return step