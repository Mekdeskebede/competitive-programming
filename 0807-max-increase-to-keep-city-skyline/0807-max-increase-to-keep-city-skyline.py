class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total = 0
        top = []
        bottom = []

        for i in range(n):
            value = 0
            for j in range(n):
                if grid[i][j] > value:
                    value = grid[i][j]
            top.append(value)
            
        for j in range(n):
            value = 0
            for i in range(n):
                if grid[i][j] > value:
                    value = grid[i][j]
            bottom.append(value)

        for i in range(n):
            for j in range(n):
                total += min(top[i],bottom[j]) - grid[i][j]        

        return total