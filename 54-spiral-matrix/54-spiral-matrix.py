class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        left_row = 0
        right_row = len(matrix[0]) - 1
        top_col = 0
        bottom_col = len(matrix) - 1
        ans = []
        
        while left_row <= right_row and top_col <= bottom_col:
            
            for i in range(left_row, right_row + 1):
                ans.append(matrix[top_col][i])
            top_col += 1
            
            for i in range(top_col,bottom_col + 1):
                ans.append(matrix[i][right_row])
                
            right_row -= 1
            
            if not (top_col <= bottom_col and left_row <= right_row):
                break
                
            for i in range(right_row, left_row-1,-1):
                ans.append(matrix[bottom_col][i])
            bottom_col -= 1
            
            # if left_row <= right_row:
                
            for i in range(bottom_col, top_col-1,-1):
                ans.append(matrix[i][left_row])
            left_row += 1
            
        return ans
                    
                
                
            
            