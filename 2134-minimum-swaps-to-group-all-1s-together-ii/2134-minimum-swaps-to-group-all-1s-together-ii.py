class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = sum(nums)
        if ones == 0:
            return 0
        nums[:ones]
        res = nums[:ones].count(0)
        count = res
        l = 0
        for r in range(ones, 2*n):
            if nums[l%n] == 0: count -= 1
            if nums[r%n] == 0:
                count += 1
            res = min(res, count)
            l += 1
        return res