class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c]:
                    s = min(matrix[r-1][c], matrix[r][c-1])
                    if matrix[r-s][c-s]:
                        matrix[r][c] = s + 1
                    else:
                        matrix[r][c] = s
        return sum(map(sum, matrix))