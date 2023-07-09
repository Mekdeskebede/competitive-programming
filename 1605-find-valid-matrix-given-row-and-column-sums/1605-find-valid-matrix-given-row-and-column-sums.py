class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        ans = [[0]*len(colSum) for i in range(len(rowSum))]
        p1 = 0
        p2 = 0
        
        while p1 < len(rowSum) and p2 < len(colSum):
            ans[p1][p2] = min(rowSum[p1], colSum[p2])
            if rowSum[p1] == colSum[p2]:
                p1 += 1
                p2 += 1
            elif rowSum[p1] > colSum[p2]:
                rowSum[p1] -= colSum[p2]
                p2 += 1
            else:
                colSum[p2] -= rowSum[p1]
                p1 += 1

        return ans