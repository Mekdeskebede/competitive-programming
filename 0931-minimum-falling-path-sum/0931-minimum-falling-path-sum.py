class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                mini = matrix[i-1][j]
                if j > 0:
                    mini = min(mini, matrix[i-1][j-1])
                if j < n-1:
                    mini = min(mini, matrix[i-1][j+1])
                matrix[i][j] += mini
        return min(matrix[-1])
        