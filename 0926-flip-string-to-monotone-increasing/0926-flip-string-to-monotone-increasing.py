class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0
        res = 0            
                                            
        for num in s:                      
                                            
            if num =='1': ones += 1         
                                      
            elif ones:        
                ones -= 1                  
                res += 1          
                                           
        return res