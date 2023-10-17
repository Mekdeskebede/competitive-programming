class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        totalSum = sum(nums)
        if totalSum%2 != 0:
            return False
        target = totalSum//2
        
        @cache 
        def dfs(i,currSum,target):
            if currSum == target:
                return True
            if i >= len(nums) or target < currSum:
                return False
            ans = dfs(i+1,currSum,target) or dfs(i+1,currSum+nums[i],target)
            return ans
        
        return dfs(0,0,target)