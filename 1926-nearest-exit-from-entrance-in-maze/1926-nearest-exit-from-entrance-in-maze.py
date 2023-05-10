class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        n = len(maze)
        m = len(maze[0])
        directions = [[-1,0], [0,-1], [1,0], [0,1]]
        def inBound(row,col):
            return 0 <= row < n and 0 <= col < m
        
        def isBorder(row,col):
            return row == 0 or col == 0 or row == n-1 or col == m-1
            
        visited = set((entrance[0],entrance[1]))
        queue = deque([[entrance[0],entrance[1],0]])
        while queue:
            
            row, col, distance = queue.popleft()
            for r, c in directions:
                if inBound(row+r, col+c) and maze[row+r][col+c] == '.' and (row+r, col+c) not in visited:
                    if isBorder(row+r, col+c) and (row + r, col + c) != (entrance[0], entrance[1]):
                        
                        return distance + 1
                    queue.append([row+r, col+c, distance+1])
                    visited.add((row+r, col+c))
       
        return -1
                
            
            