class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        def inBound(row,col):
            return 0 <= row < n and 0 <= col < m

        dp = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(int(matrix[i][j]))
            dp.append(temp)
        
        for row in range(n-1,-1,-1):
            for col in range(m-1,-1,-1):
                if not inBound(row,col+1) or not inBound(row+1, col) or not inBound(row+1,col+1) or matrix[row][col] == "0":
                    continue
                dp[row][col] = 1 + int(min(dp[row+1][col],dp[row][col+1],dp[row+1][col+1]))
                
        max_ = 0
        for i in range(n):
            max_ = max(max_, max(dp[i]))
            
        return max_ * max_
                
        