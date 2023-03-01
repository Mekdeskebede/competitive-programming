class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
         
        n = len(nums)
        for i in range(1,n):
            nums[i] += nums[i-1]
        
        pre_sum = defaultdict(int,{0:1})
        windows = 0
        for num in nums:
            if num%k in pre_sum:
                windows += pre_sum[num%k]
            pre_sum[num%k] += 1
        
        return windows
            