class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0 
        for idx,row in enumerate(grid):
            l,h = 0,len(row)-1
            
            while l <= h:
                mid = l + (h-l)//2
                if grid[idx][mid] >= 0:
                    l = mid + 1
                elif grid[idx][mid] < 0:
                    h = mid - 1
            res += len(row) - l
        return res
            