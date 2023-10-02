class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = s
        text2 = s[::-1]
        dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        
        for row in range(len(text2)-1,-1,-1):
            for col in range(len(text1)-1,-1,-1):
                if text1[col] == text2[row]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])
                        
        return dp[0][0]