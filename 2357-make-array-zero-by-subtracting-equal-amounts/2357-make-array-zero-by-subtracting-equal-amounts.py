class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        num = set(nums)
        res = len(num)
        num = list(nums)
        num.sort()
        if num[0] == 0:
            res -= 1
        return res