class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
        
        def available(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0])
        
        def reveal(board, x, y):
            if not available(x, y) or board[x][y] != "E":
                return
            mine_count = 0
            for dx, dy in directions:
                if available(dx+x, dy+y) and board[dx+x][dy+y] == "M":
                    mine_count += 1
            if mine_count:
                board[x][y] = str(mine_count)
            else:
                board[x][y] = "B"
                for dx, dy in directions:
                    reveal(board, dx+x, dy+y)

        if board[x][y] == "M":
            board[x][y] = "X"
        elif board[x][y] == "E":
            reveal(board, x, y)
        return board