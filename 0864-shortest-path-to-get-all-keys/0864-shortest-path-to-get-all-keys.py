class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        keyPairs = {chr(i):chr(i+32) for i in range(65,91)}
        n = len(grid)
        m = len(grid[0])
        
        def inBound(row,col):
            return 0 <= row < n and 0 <= col < m
        
        countKeys = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "@":
                    start = (row,col)
                elif grid[row][col].islower():
                    countKeys += 1
        queue = deque([[start[0], start[1], 0, 0]])
        visited = set([(start[0], start[1], 0)])
        
        while queue:
            row, col, move,keys = queue.popleft()
            if keys == (1 << countKeys) - 1:
                    return move
        
            for r, c in directions:
                if inBound(row+r, col+c) and grid[row+r][col+c] != "#":
                    newKeys = keys
                    if grid[row+r][col+c].islower():
                        newKeys |= 1 << (ord(grid[row+r][col+c]) - ord('a'))
                    if grid[row+r][col+c].isupper() and not (keys >> (ord(grid[row+r][col+c]) - ord('A')) & 1):
                            continue
                    if (row+r, col+c,newKeys) not in visited:
                        queue.append([row+r, col+c,move+1, newKeys])
                        visited.add((row+r, col+c,newKeys))
            
        return -1