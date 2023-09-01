class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = {}
        max_ = 1
        for i in range(len(arr)):
            if (arr[i] - difference) in dp:
                dp[arr[i]] = 1 + dp[arr[i] - difference]
                max_ = max(max_, dp[arr[i]])
            else:
                dp[arr[i]] = 1
           
            
        return max_
        