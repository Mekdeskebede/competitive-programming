class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count = {}
        l = 0
        total = 0
        maxSum = 0
        
        for r in range(len(nums)):
            total += nums[r]
            count[nums[r]] = count.get(nums[r],0) + 1
            while len(count) < r - l + 1:
                total -= nums[l]
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                l += 1
            maxSum = max(maxSum, total)

        return maxSum
            
            
                
            