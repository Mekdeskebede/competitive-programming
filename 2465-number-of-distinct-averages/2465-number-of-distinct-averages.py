class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res = []
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            ave = (nums[l] + nums[r]) / 2
            if ave not in res:
                res.append(ave)
            l += 1
            r -= 1
        return len(res)
        