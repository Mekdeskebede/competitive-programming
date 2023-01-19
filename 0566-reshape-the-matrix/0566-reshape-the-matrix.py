class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        n = len(mat)
        m = len(mat[0])
        
        if r*c != m*n:
            return mat
        
        oneD = [0  for j in range(m*n)]
        for row in range(n):
            
            for col in range(m):
                
                unique = row*m + col
                oneD[unique] = mat[row][col]
                
        ans = [[0 for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                
                ans[i][j] = oneD[c*i + j]
                
        return ans
                
                