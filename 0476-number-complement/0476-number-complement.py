class Solution:
    def findComplement(self, num: int) -> int:
        
        s = ""
        while num > 0:
            if (num & 1) == 1:
                s += "0"
            else:
                s += "1"
            num >>= 1
            
        s = s[::-1]
        s = int(s,2)
        
        return s