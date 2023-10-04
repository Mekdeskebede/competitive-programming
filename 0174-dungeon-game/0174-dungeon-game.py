class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n = len(dungeon)
        m = len(dungeon[0])
        
        def inBound(row,col):
            return  0 <= row < n and 0 <= col < m
                       
        for row in range(n-1,-1,-1):
            for col in range(m-1,-1,-1):
                if inBound(row+1,col) and inBound(row,col+1):
                    maxi = max(dungeon[row+1][col],dungeon[row][col+1])
                    dungeon[row][col]= 0 if maxi+dungeon[row][col] >= 0 else maxi+dungeon[row][col]
                    
                elif inBound(row+1,col):
                    dungeon[row][col] = 0 if dungeon[row][col] + dungeon[row+1][col] >= 0 else dungeon[row][col] + dungeon[row+1][col]
                
                elif inBound(row,col+1):
                    dungeon[row][col] = 0 if dungeon[row][col] + dungeon[row][col+1] >= 0 else dungeon[row][col] + dungeon[row][col+1]
                
                else:
                    dungeon[row][col] = 0 if dungeon[row][col] >= 0 else dungeon[row][col]
                            
        return - dungeon[0][0] + 1

                
                