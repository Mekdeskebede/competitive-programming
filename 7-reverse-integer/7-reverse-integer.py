class Solution:
    def reverse(self, x: int) -> int:
        
        temp = abs(x)
        temp = str(temp)
        
        temp= temp[::-1]
        temp = int(temp)
    
        if x < 0:     
            temp = -1 * temp
        return temp if -2147483648 < temp < 2147483648 else 0
        
            