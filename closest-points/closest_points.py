from cmath import sqrt
from locale import currency

class Solution(object):
    def kClosest(selef,points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        closest = []
    
        for i in range(k):
        
            close_distance = pow((pow(points[0][0],2)+pow(points[0][1],2)), 0.5)
            curr_closest = [] 
            

            for k,j in points:
                distance = pow((pow(k,2)+pow(j,2)), 0.5)
            
                if distance <= close_distance:
                    close_distance = distance
                    curr_closest = []
                    curr_closest.append(k)
                    curr_closest.append(j)
                    
                else:
                    continue
            
            closest.append(curr_closest)
            points.pop(points.index(curr_closest))
            


        return closest

