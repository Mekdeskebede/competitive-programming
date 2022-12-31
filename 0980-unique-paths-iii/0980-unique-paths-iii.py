class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.depth = 0

        def dfs(row, col, non_obstacles):

            if grid[row][col] == 2 and non_obstacles == 1:
                self.depth += 1
                return

            temp = grid[row][col]
            grid[row][col] = -1
            non_obstacles -= 1

            for index1, index2 in directions:

                next_row = index1 + row
                next_col = index2 + col

                if next_row in range(len(grid)) and next_col in range(len(grid[0])) and grid[next_row][next_col] != -1:
                       
                        dfs(next_row, next_col, non_obstacles)

            grid[row][col] = temp

            return self.depth

        non_obstacles = 0
        for row in range(len(grid)):

            for col in range(len(grid[0])):

                if grid[row][col] == 1:
                    result = [row, col]
                if grid[row][col] >= 0:
                    non_obstacles += 1

        return dfs(result[0], result[1], non_obstacles)