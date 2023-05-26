class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        path = {
            1:{"l":[4,6,1], 'r':[3,5,1] ,'b': [],'t':[]},
            2:{"l":[],'r':[],'b': [5,6,2],'t':[3,4,2]}, 
            3:{"l":[4,1,6],'r':[],'b': [5,6,2],'t':[]},
            4:{"l":[],'r':[3,1,5],'b': [5,6,2],'t':[]},
            5:{"l":[4,6,1],'r':[],'b': [],'t':[2,3,4]}, 
            6:{"l":[],'r':[3,5,1],'b': [],'t':[2,3,4]}
        }
    
        
        visited = set()
        n = len(grid)
        m = len(grid[0])
        
        def inBound(row,col):
            return 0 <= row < n and 0 <= col < m
        
        def dfs(row, col):
            nonlocal isPossible
            if row == n-1 and col == m-1:
                return True
            dr = grid[row][col]
            for r in path[dr]["r"]:
                if inBound(row, col+1) and (row, col+1) not in visited and dr in path[grid[row][col+1]]['l']:
                    visited.add((row, col+1))
                    if dfs(row, col+1):
                        return True
                    
            for l in path[dr]['l']:
                if inBound(row, col-1) and (row, col-1) not in visited and dr in path[grid[row][col-1]]['r']:
                    visited.add((row, col-1))
                    if dfs(row, col-1):
                        return True
                    
            for t in path[dr]['t']:
                if inBound(row-1, col) and (row-1, col) not in visited and dr in path[grid[row-1][col]]['b']:
                    visited.add((row-1, col))
                    if dfs(row-1, col):
                        return True
                    
            for b in path[dr]['b']:
                if inBound(row+1, col) and (row+1, col) not in visited and dr in path[grid[row+1][col]]['t']:
                    visited.add((row+1, col))
                    if dfs(row+1, col):
                        return True
            return False
                    
        isPossible = False
        visited.add((0,0))
        return dfs(0,0)
        
        
