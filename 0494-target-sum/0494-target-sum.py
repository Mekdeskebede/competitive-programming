class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def backTrack(i,total):
            if i == len(nums):
                if target == total:
                    return 1
                return 0
            
            if (i,total) not in dp:
                dp[(i,total)] = backTrack(i+1,total+nums[i]) + backTrack(i+1,total-nums[i])
                
            return dp[(i,total)]
            
        return backTrack(0,0)
            