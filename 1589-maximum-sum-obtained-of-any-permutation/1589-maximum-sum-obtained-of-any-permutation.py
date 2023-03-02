class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        n = len(nums)
        frequency = [0] * n
        
        for start, end in requests:
            frequency[start] += 1
            if end+1 < n:
                frequency[end+1] -= 1
        
        for i in range(1,n):
            frequency[i] += frequency[i-1]
            
        frequency.sort()
        nums.sort()
        ans = 0
        
        for i in range(n):
            ans += (nums[i] * frequency[i])
            
        return int(ans %int(1e9 + 7))

