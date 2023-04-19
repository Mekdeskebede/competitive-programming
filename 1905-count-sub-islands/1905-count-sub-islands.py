class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        n = len(grid1)
        m = len(grid1[0])
        
        def inBound(row,col):
            return 0 <= row < n and 0 <= col < m
        
        def dfs(row, col):
            grid2[row][col] = 0
            if grid1[row][col] == 0:
                self.subIsland = False
            for r, c in directions:
                if inBound(row+r, col+c) and grid2[row+r][col+c] == 1:
                    dfs(row+r, col+c)
        
        ans = 0
        for row in range(n):
            for col in range(m):
                self.subIsland = True
                if grid2[row][col] == 1:
                    dfs(row,col)
                else:
                    self.subIsland = False
                if self.subIsland:
                    ans += 1
        return ans
            