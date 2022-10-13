class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        res = 0
        while left < right:
            add = nums[left] + nums[right]
            if add == k:
                res += 1
                right -= 1
                left += 1
            elif add > k:
                right -= 1
            else:
                left += 1
        return res
            