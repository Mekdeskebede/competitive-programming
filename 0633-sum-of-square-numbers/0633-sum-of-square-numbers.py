class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0
        right = int(sqrt(c))
        while left <= right:
            
            square = left**2 + right**2 
            
            if square == c:
                return True
            elif square  > c:
                right -= 1
            else:
                left += 1
        return False