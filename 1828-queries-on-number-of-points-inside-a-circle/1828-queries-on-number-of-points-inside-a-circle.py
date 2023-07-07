class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for x,y,r in queries:
            inside = 0
            for x2,y2 in points:
                ec = sqrt((x2-x)**2 + (y2-y)**2)
                if ec <= r:
                    inside += 1
            ans.append(inside)
            
        return ans