class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        k_sum = sum(nums[:k])
        max_sum = k_sum
        
        left = 0
        for right in range(k,n):
            k_sum -= nums[left]
            k_sum += nums[right]
            max_sum = max(max_sum,k_sum)
            left += 1    
            
        return max_sum/k