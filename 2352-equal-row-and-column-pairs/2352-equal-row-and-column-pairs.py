class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        rows = Counter(map(tuple,grid))
        count = 0
        
        for col in range(m):
            column = []
            
            for row in range(n):
                column.append(grid[row][col])
                
            if tuple(column) in rows:
                count += rows[tuple(column)]
        
        return count