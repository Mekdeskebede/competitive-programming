class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        left = 0
        right = 0
        ans = 0
        add = 0
        while right < len(nums):
            add += nums[right] 
            while nums[right] * (right - left + 1) > add + k:
                add -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
            
        return ans
            