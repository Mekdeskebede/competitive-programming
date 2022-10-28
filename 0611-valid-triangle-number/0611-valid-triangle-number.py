class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        if n < 3:
            return res
        nums.sort()
        for i in range(n-1,1,-1):
            
            l = 0
            r = i - 1
            while l < r:
                if nums[i] < nums[l]+ nums[r]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res
            
            