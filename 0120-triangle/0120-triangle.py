class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[-1]]
        
        for i in range(len(triangle)-2,-1,-1):
            temp = []
            for j in range(len(triangle[i])):
                curr = triangle[i][j] + min(dp[-1][j],dp[-1][j+1])
                temp.append(curr)
            dp.append(temp)
            
        return dp[-1][-1]