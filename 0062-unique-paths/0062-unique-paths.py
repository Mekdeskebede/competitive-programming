class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        
        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        def backTrack(row,col):
            if  row == 0 and col == 0:
                return 1
            if (row, col) not in dp:
                rw = 0
                cl = 0
                if inBound(row-1,col):
                    rw = backTrack(row-1,col)
                if inBound(row, col-1):
                    cl = backTrack(row, col-1)
                dp[(row,col)] = rw + cl
            return dp[(row,col)] 

        return backTrack(m-1,n-1)

             