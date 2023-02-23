class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.matrix = matrix
        n = len(self.matrix)
        m = len(self.matrix[0])
        
        self.prefix = [[0 for i in range(m+1)] for j in range(n+1)]
        
        for row in range(n):
            for col in range(m):
                
                self.prefix[row+1][col+1] = self.matrix[row][col] + self.prefix[row+1][col] + self.prefix[row][col+1] - self.prefix[row][col]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1
        
        return self.prefix[row2][col2] - self.prefix[row2][col1-1] - self.prefix[row1-1][col2] + self.prefix[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)