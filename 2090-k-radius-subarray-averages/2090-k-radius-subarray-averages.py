class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        if k * 2 + 1 > len(nums):
            return res
        total = sum(nums[:k*2 + 1])
        res[k] = total//(k*2 + 1)
        l = 0
        ptr = k+1
        for r in range(k*2+1, len(nums)):
            total += nums[r] - nums[l]
            res[ptr] = total//(k*2 + 1)
            l += 1
            ptr += 1
        return res