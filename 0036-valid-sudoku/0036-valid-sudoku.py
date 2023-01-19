class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        m = len(board[0])
        
        for row in board:
            visited = set()
            for num in row:
                
                if num != '.':
                    if num in visited:
                        return False
                    visited.add(num)
                
        for col in range(m):
            visited = set()
            for row in range(n):
                
                if board[row][col] != '.':
                    if board[row][col] in visited:
                        return False
                    visited.add(board[row][col])
       
        for i in range(0,9,3):
            for j in range(0,9,3):
                
                visited = set()
                for k in range(i,i+3):
                    for l in range(j, j+3):
                        
                        if board[k][l] != '.':
                            if board[k][l] in visited:
                                return False
                            visited.add(board[k][l])
        return True

                
            