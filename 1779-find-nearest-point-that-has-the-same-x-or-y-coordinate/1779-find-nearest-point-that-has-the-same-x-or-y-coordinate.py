class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        ans = [float('inf'), None]
        for indx,(a,b) in enumerate(points):
            if a == x or y == b:
                manh = abs(x-a) + abs(y-b)
                if manh < ans[0]:
                    ans = [manh,indx]
        if ans[0] != float('inf'):
            return ans[1]
        else:
            return -1
        