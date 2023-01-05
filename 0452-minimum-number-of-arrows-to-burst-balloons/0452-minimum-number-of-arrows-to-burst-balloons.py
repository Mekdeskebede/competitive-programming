class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key= lambda x:x[1])
        shoot = 1
        x_axis = points[0][1]
        
        for start, end in points:

            if x_axis < start:
                shoot += 1
                x_axis = end
                
        return shoot
    
                
                