class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        first = -1 
        ans = 0
        for i in bank:
            
            count = i.count("1")
            
            if count != 0:
                if first == -1:
                    first = count  
                else:
                    ans += (first*count)
                    first = count
        
        return ans