class Solution:
    
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)  - 2
        ans = []
        
        for i in range(n):
            temp = []
            
            for j in range(n):
                max_elt = float(-inf)
                
                for m in range(i,i + 3):
                    for k in range(j,j + 3):
                        max_elt = max(max_elt, grid[m][k])
                        
                temp.append(max_elt)
            ans.append(temp)
            
        return ans
                    

                