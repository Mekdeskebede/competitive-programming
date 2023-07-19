class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        board = tuple(j for i in board for j in i)
        directions = {0:[1, 3], 1:[0, 2, 4], 2:[1, 5], 3:[0, 4], 4:[1, 3, 5], 5: [4, 2]}
        zero_index = board.index(0)
        queue = deque([[board, 0, zero_index]]) # tupple, number of steps, number 0 index
        visited_boards = set([board])
        
        while queue:
            board, moves, zero_index = queue.popleft()
            if board == (1,2,3,4,5,0):
                return moves
            
            for index in directions[zero_index]:
                board_list = list(board)
                (board_list[index], board_list[zero_index]) = (board_list[zero_index], board_list[index])
                
                new_board = tuple(board_list)
                if new_board not in visited_boards:
                    visited_boards.add(new_board)
                    queue.append([new_board, moves + 1, index])
                    
        return -1
