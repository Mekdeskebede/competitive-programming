class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n == 1:
            return True
        if n%3 != 0:
            return False
        while n >= 3:
            n = n/3
       
        
        if  n == 1.0:
            
            return True
        else:
            
            return False
        
            