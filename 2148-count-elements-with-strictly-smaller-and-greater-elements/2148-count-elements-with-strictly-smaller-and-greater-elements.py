class Solution:
    def countElements(self, nums: List[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        count = 0
        for i in nums:
            if i == mini or i == maxi:
                count += 1
        return len(nums) - count