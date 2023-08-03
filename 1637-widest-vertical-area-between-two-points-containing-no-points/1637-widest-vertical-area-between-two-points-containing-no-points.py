class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        newPoints = [i for [i,j] in points]
        newPoints.sort()
        thick = 0
        for i in range(1,len(newPoints)):
            thick = max(thick, newPoints[i] - newPoints[i-1])

        return thick