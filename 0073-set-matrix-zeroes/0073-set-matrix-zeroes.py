class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        rows = set()
        cols = set()
    
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)
                    
        for row in range(n):
            for col in range(m):
                if row in rows or col in cols:
                    matrix[row][col] = 0
                    
                    
        
        