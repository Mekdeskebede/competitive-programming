class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
     
        n = len(matrix)
        
        matrix.reverse()
        
        for row in range(n):
            for col in range(row):
                
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col] 
