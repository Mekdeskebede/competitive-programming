class Solution:
    def countDigits(self, num: int) -> int:
        
        num_string = str(num)
        count = 0
        
        for i in num_string:
            if num%int(i) == 0:
                count += 1
                
        return count