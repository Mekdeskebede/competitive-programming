class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(mat)
        m = len(mat[0])
        prefix = [[0 for i in range(m+1)] for j in range(n+1)]
        
        for row in range(n):
            for col in range(m):
                
                prefix[row+1][col+1] = mat[row][col] + prefix[row+1][col] + prefix[row][col+1] - prefix[row][col]
                
        print(prefix)
        
        ans = [[0]*m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                
                row1 = i-k
                row2 = i+k
                col1 = j-k
                col2 = j+k
                
                if row1 < 0:
                    row1 = 0
                if row2 >= n:
                    row2 = n -1 
                if col1 < 0:
                    col1 = 0
                if col2 >= m:
                    col2 = m - 1
                
                row1 += 1
                row2 += 1
                col1 += 1
                col2 += 1
                
                ans[i][j] = prefix[row2][col2] - prefix[row2][col1-1] - prefix[row1-1][col2] + prefix[row1-1][col1-1]
        
        return ans
                
                
                
                