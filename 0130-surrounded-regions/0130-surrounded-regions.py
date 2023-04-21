class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        n = len(board)
        m = len(board[0])
        
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        def dfs(row,col):
            if board[row][col] == "O":
                board[row][col] = False
            for r, c in directions:
                if inBound(row+r, col+c) and board[row+r][col+c] == "O":
                    dfs(row+r, col+c)
        
        for i in range(n):
            if board[i][0] == "O":
                dfs(i,0)
        for i in range(m):
            if board[0][i] == "O":
                dfs(0,i)
        for i in range(n):
            if board[i][m-1] == "O":
                dfs(i,m-1)
        for i in range(m):
            if board[n-1][i] == "O":
                dfs(n-1,i)
        print(board)
        for row in range(n):
            for col in range(m):
                if board[row][col] == False:
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"
                
                
                