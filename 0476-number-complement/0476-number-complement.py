class Solution:
    def findComplement(self, num: int) -> int:
        
        val = 0
        original = num
        
        while  original >= (1<<val) :
            num = (1<<val) ^ num
            val += 1
        return num