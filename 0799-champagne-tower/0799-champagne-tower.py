class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = []
        for i in range(1,101):
            dp.append([0]*i)
        
        dp[0] = [poured]
        i = 0
        while i < len(dp) and i <= query_row:
            for j in range(len(dp[i])):
                if dp[i][j] > 1:
                    excess = dp[i][j] - 1
                    dp[i][j] = 1
                    if i + 1 < len(dp):
                        dp[i+1][j] += excess/2
                        dp[i+1][j+1] += excess/2
            i += 1
        return dp[query_row][query_glass]
        