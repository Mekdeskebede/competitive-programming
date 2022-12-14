class Solution:
    def rob(self, nums: List[int]) -> int:
        first , last = 0, 0
        for num in nums:
            temp = max(num + first, last)
            first = last
            last = temp
        return last
        