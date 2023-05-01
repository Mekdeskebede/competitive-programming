class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        fresh = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        for row in range(n):
            for col in range(m):
                
                if grid[row][col] == 2:
                    queue.append((row,col, 0))
                elif grid[row][col] == 1:
                    fresh += 1
        
        def inBound(row,col):
            return 0 <= row < n and 0 <= col < m
                    
        if not queue and fresh:
            return -1
        if not fresh:
            return 0
        
        steps = 0
        while queue:
            row,col, time = queue.popleft()
            for r,c in directions:
                if inBound(r+row,c+col) and grid[row+r][col+c] == 1:
                    fresh -= 1
                    queue.append((row+r,col+c, time + 1))
                    grid[row+r][col+c] = 2
                    
        if fresh:
            return -1
        return time
                
                
                