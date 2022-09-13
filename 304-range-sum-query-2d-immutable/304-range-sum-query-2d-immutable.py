class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.preMat = [[0] * (len(matrix[0]) +1) for i in range(len(matrix)+1)]
        for i in range(len(matrix)):
            sum1 = 0
          
            for j in range(len(matrix[0])):
                sum1 += matrix[i][j]
                self.preMat[i+1][j+1] = sum1 + self.preMat[i][j+1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
       
        return (self.preMat[row2+1][col2+1]) - (self.preMat[row1][col2+1]) - (self.preMat[row2+1][col1]) + (self.preMat[row1][col1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)