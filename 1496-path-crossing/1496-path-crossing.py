class Solution:
    def isPathCrossing(self, path: str) -> bool:
        currX = 0
        currY = 0
        visited = set([(0,0)])
        for p in path:
            if p == "N":
                currY += 1
            elif p == "E":
                currX += 1
            elif p == "W":
                currX -= 1
            else:
                currY -= 1
            if (currX,currY) in visited:
                return True
            visited.add((currX,currY))
            
        return False
        