class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        primes = [True] * (right + 1)
        
        primes[0] = primes[1] = False
        
        i = 2
        while i * i <= right:
            if primes[i]:
                j = i * i
                while j <= right:
                    primes[j] = False
                    j += i
            i += 1
        
        leftToRight = []
        for p in range(len(primes)):
            if primes[p] and left <= p <= right:
                leftToRight.append(p)
                
        if len(leftToRight) < 2:
            return [-1,-1]
        mini = [leftToRight[0],leftToRight[1], leftToRight[1]-leftToRight[0]]
        
        for i in range(1,len(leftToRight) - 1):
            if mini[2] > leftToRight[i+1]-leftToRight[i]:
                mini = [leftToRight[i],leftToRight[i+1], leftToRight[i+1]-leftToRight[i]]
        return mini[:2]