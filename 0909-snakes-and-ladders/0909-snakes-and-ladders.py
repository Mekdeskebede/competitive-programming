class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        seen = set()
        bfs = deque()
        bfs.append(1)
        n = len(board)
        steps = 0
        k = 1
        while(len(bfs)!=0):
            for _ in range(k):
                currBox = bfs[0]
                bfs.popleft()
                if currBox == n*n:
                    return steps
                if currBox in seen:
                    continue
                seen.add(currBox)
                for j in range(currBox+1,min((n*n)+1,currBox + 7)):
                    row =  ceil(j/n)
                    col = j%n
                    if row%2 == 1:
                        if board[n-row][col-1]!=-1:
                            bfs.append(board[n-row][col-1])
                            continue
                    else:
                        if col == 0:
                            col = n
                        if board[n-row][n-col]!=-1:
                            bfs.append(board[n-row][n-col])
                            continue
                    bfs.append(j)
            k = len(bfs)
            print(k)
            steps+=1
        return -1