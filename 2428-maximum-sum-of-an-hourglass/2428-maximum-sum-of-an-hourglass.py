class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n = len(grid) - 2
        m = len(grid[0]) - 2
        
        res = 0
        for i in range(n):
            for j in range(m):
                total = sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3])
                res = max(res,total)
        return res