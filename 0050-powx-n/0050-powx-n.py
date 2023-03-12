class Solution:
    def power(self,x,n):

        if n <= 1:
            return x
        temp = self.power(x,n//2)
        if n%2 == 0:
            return temp * temp
        else:
            return temp * temp * x
        
            
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 1:
            return 1/self.power(x,-n)
        else:
            return self.power(x,n)
        
        
            