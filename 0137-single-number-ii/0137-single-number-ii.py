class Solution:
        
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            one = num ^ ones
            one = one & ~twos
            ones = one
            two = num ^ twos
            two = two & ~ones
            twos = two
            
        return ones
            
            
        