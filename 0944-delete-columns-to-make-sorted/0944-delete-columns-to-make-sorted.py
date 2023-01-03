class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        column = 0
        for col in range(len(strs[0])):
            
            for row in range(len(strs)-1):
                
                if ord(strs[row][col])>ord(strs[row+1][col]):
                    
                    print(strs[row][col],strs[row+1][col])
                    column += 1
                    break
        return column