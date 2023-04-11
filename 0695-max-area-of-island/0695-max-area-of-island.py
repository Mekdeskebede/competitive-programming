class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        
        def inBound(row,col):
            return (0 <= row< len(grid)) and (0 <= col < len(grid[0]))
        
        def dfs(row,col):
            count = 0
            grid[row][col] = 0
            
            for r, c in directions:
                if inBound(row+r, col+c) and grid[row+r][col+c]==1:
                    count += dfs(row+r, col+c)
                    
            return count + 1

                    
        maximum = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maximum = max(maximum, dfs(row,col))
                    
        
        return maximum
                
            
        