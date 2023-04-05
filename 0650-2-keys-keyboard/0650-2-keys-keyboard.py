class Solution:
    def minSteps(self, n: int) -> int:
        
        if n == 1:
            return 0
        primes = 0
        
        d = 2
        while d*d <= n:
            while n % d == 0:
                primes += d
                n //= d
            d += 1
            
        if n > 1:
            primes += n
        
        return primes
            
        
        
            