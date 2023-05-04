class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        directions = [[1,0],[0,1],[1,1],[-1,-1],[-1,0], [0,-1],[1,-1],[-1,1]]
        queue = deque([[0,0,1]])
        visited = set()
        visited.add((0,0))
        
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < n
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        while queue:
            row, col, pathLen = queue.popleft()
            if grid[row][col] == 1:
                return -1
            if row == n-1 and col == n-1:
                return pathLen
                            
            for r, c in directions:
                if inBound(r+row, col+c) and grid[row+r][col+c] == 0 and (row+r,col+c) not in visited:
                    queue.append([row+r,col+c,pathLen+1])
                    visited.add((row+r,col+c))

        return -1