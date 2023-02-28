class Solution:
    def getRow(self, rowIndex: int) -> List[int]: 
        table = [[0] * (i + 1) for i in range(0, rowIndex + 1)]
        table[0] = [1]
        for i in range(1, rowIndex + 1):
            for j in range(len(table[i])):
                if j == 0 or j == len(table[i]) - 1:
                    table[i][j] = 1
                else:
                    table[i][j] = table[i - 1][j - 1] + table[i - 1][j]
        return table[-1]
        
        
        
        