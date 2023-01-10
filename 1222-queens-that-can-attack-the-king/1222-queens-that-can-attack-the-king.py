class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        queens = set(tuple(q) for q in queens)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        attackers = []
        
        for tempX, tempY in directions:
            x, y = king
            while(0<=x<8 and 0<=y<8):
                x += tempX
                y += tempY
                if (x, y) in queens:
                    attackers.append([x, y])
                    break
        return attackers