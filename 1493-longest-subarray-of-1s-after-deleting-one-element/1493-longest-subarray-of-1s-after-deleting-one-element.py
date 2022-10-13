class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        zero = 1
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero -= 1

            while zero < 0 and left <= right:
                if nums[left] == 0:
                    zero += 1
                left += 1
            res = max(res, right-left)
            
        return res