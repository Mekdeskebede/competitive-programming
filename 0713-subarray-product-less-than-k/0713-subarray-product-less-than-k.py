class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        res = 0
        mul = 1
        
        while right < len(nums):
            if k <= 1:
                return 0
            mul *= nums[right]
            
            while mul >= k :
                mul /= nums[left]
                left += 1 
            res += right - left + 1
            right += 1
        return res
            