class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        first = -1 
        ans = 0
        for i in bank:
            
            temp = i.count("1")
            
            if temp != 0:
                if first == -1:
                    first = temp  
                else:
                    ans += (first*temp)
                    first = temp
        
        return ans