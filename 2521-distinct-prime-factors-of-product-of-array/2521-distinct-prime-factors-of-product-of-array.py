class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        distinct = set()
        
        for num in nums:
            
            d = 2
            while d * d <= num: 
                while num % d == 0:
                    distinct.add(d)
                    num //= d
                d += 1
                
            if num > 1:
                distinct.add(num)
                
        return len(distinct)