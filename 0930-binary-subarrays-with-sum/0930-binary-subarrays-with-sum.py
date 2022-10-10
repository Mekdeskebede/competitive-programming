class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        preSum = []
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            preSum.append(add)
            
        visited = defaultdict(int)
        visited[0] = 1
        res = 0
        for i in range(len(nums)):
            diff = preSum[i] - goal
            if diff in visited:
                res += visited[diff]
            
            visited[preSum[i]] += 1
        
        return res 