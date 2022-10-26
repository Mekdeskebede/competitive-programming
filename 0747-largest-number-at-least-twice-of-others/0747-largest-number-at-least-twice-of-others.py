class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi = max(nums)
        idx = None
        for i in range(len(nums)):
            if nums[i] == maxi:
                idx = i
            elif maxi/2 < nums[i]:
                return -1
        return idx