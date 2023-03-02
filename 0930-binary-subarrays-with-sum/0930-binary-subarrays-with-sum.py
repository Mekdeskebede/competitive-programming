class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        n = len(nums)
        sum_count = {0:1}
        
        for i in range(1,n):
            nums[i] += nums[i-1]
     
        ans = 0
        for num in nums:
            if num - goal in sum_count:
                ans += sum_count[num - goal]
            sum_count[num] = 1 + sum_count.get(num,0)

        return ans
                