class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        maximum = max(nums)
        minimum = min(nums)
        
        def GCD(maximum, minimum):
            if minimum == 0:
                return maximum
            
            maximum , minimum = minimum,maximum%minimum
            return GCD(maximum,minimum)
        
        return GCD(maximum,minimum)
                
                
                
        