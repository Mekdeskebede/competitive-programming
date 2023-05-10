class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        n = len(mat)
        m = len(mat[0])
        ans = [[0 for i in range(m)] for j in range(n)]
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        queue = deque()
        visited = set()
        for row in range(n):
            for col in range(m):
                if mat[row][col] == 0:
                    queue.append((row,col,0))
                    
        while queue:
            row,col,distance = queue.popleft()
            ans[row][col] = distance
            
            for r, c in directions:
                if inBound(r+row, c+col) and (r+row, c+col) not in visited and mat[r+row][c+col]==1:
                    queue.append([r+row, c+col,distance+1])
                    visited.add((r+row, c+col))    
                    
        return ans     