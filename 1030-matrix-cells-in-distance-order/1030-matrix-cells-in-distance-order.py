class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        matrix = []
        res = []
        d = {}
        
        for i in range(rows):
            for j in range(cols):
                matrix.append([i,j])
                
        for row in matrix:
            distance = abs(rCenter - row[0]) + abs(cCenter - row[1])
            if distance in d:
                d[distance].append(row)
            else:
                d[distance] = []
                d[distance].append(row)
                
        for i in range(len(d)):
            for j in d[i]:
                res.append(j)
        return res