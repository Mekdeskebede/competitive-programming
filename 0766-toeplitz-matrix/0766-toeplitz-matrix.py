class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])
        top_left = {}
        
        for row in range(n):
            for col in range(m):
                if col-row in top_left:
                    if top_left[col-row] != matrix[row][col]:
                        return False
                else:
                    top_left[col-row] = matrix[row][col]
        return True
                    
                    
                    