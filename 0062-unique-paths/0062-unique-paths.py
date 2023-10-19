class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {(0,0):1}
        
        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    dp[(row, col)] = 1
                    continue
                r = 0
                c = 0
                if inBound(row, col-1):
                    c = dp[row,col-1]
                if inBound(row-1, col):
                    r = dp[(row-1,col)]
                dp[(row,col)] = r + c
                
        return dp[(m-1, n-1)]