class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        left = 0
        N, M = len(matrix),len(matrix[0])
        right = (N-1)* M + (M-1)

        while left <= right:

            mid = left + (right-left)//2
            row = mid//M
            col = mid % M
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
                    
        return False