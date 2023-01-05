class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        N = len(mat)
        M = len(mat[0])
        diagonals = []
        
        for row in range(N):
            
            temp = []
            col = 0
            r = row
            
            while 0 <= r and col < M:
                temp.append(mat[r][col])
                col += 1
                r -= 1
            
            diagonals.append(temp)
            
        for col in range(1,M):
    
            temp = []
            row = N-1
            c = col
            
            while 0 <= row < N and 0 <= c < M:
                temp.append(mat[row][c])
                c += 1
                row -= 1
            
            diagonals.append(temp)
            
        ans = []
        for idx, diagonal in enumerate(diagonals):
            
            if idx %2:
                ans += diagonal[::-1]
            else:
                ans += diagonal
           
        return ans
                
        
        