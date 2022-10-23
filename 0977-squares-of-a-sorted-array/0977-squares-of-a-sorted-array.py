class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        neg = 0
        while neg < n and nums[neg] < 0:
            neg += 1
        res = []
        l = neg - 1
        r = neg
        while r < n and l >= 0:
            if nums[l] ** 2 < nums[r] ** 2:
                res.append(nums[l] ** 2)
                l -= 1
            else:
                res.append(nums[r] ** 2)
                r += 1
        if l >= 0:
            while l >= 0:
                res.append(nums[l] ** 2)
                l -= 1
        elif r < n:
            while r < n:
                res.append(nums[r] ** 2)
                r += 1
        return res
            