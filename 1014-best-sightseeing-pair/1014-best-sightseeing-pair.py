class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_ = values[0]
        dp = [values[0]]
        
        for i in range(1, len(values)):
            dp.append(max(dp[-1] , values[i] +  i))
        
        ans = 0
        for i in range(1, len(values)):
            ans = max(ans, dp[i-1]+values[i]-i)
        
        return ans
        
        