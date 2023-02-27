class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        
        mat = [ [0]* n for _ in range(n)]
        
        for row1,col1,row2,col2 in queries:
            
            mat[row1][col1] += 1
            
            if col2 + 1 < n:
                mat[row1][col2+1] -= 1
            
            if row2+1 < n:
                mat[row2+1][col1] -= 1
                
            if row2+1 < n and col2+1 < n:
                mat[row2+1][col2+1] += 1
                
        prefix = [ [0]* (n+1) for i in range(n+1)]
        
        for row in range(n):
            for col in range(n):
                
                prefix[row+1][col+1] = mat[row][col] + prefix[row+1][col] + prefix[row][col+1] - prefix[row][col]
                
                
        for row in range(n+1):
            prefix[row] = prefix[row][1:]
            
            
        return prefix[1:]