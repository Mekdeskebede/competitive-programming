class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        m = len(grid[0])
        
        row_ones = []
        for row in grid:
            row_ones.append(row.count(1))
        
        col_ones = []
        for i in range(m):
            count = 0
            for j in range(n):
                if grid[j][i] == 1:
                    count += 1
            col_ones.append(count)
        
        ans = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                ans[i][j] = row_ones[i] + col_ones[j] - (n-row_ones[i]) - (m-col_ones[j])
        
        return ans
                
                
            