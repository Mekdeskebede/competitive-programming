class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        maxLen = -1
        add = 0
        l = 0
        r = 0
        while r < len(nums):
            add += nums[r]
            while target < add and l <= r:
                add -= nums[l]
                l += 1
            if target == add:
                maxLen = max(maxLen, r - l + 1)
            r += 1
        return -1 if maxLen == -1 else len(nums) - maxLen