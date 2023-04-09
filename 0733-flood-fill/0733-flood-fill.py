class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(-1,0), (0,-1),(1,0),(0,1)]
        n = len(image)
        m = len(image[0])
        start = image[sr][sc]
        
        def inBound(row,col):
            if 0 <= row < n and 0 <= col < m:
                return True
            return False
        
        def dfs(row,col):
            if not inBound(row,col) or image[row][col] == color or image[row][col] != start:
                return 
            image[row][col] = color

            for r,c in directions:
                dfs(r+row,col+c)
                
        dfs(sr,sc)
        
        return image