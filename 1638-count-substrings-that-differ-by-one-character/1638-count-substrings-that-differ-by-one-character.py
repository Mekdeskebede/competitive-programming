class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        if s == t: return 0 
        
        ls = len(s)        
        lt = len(t)        
        ans = 0
        
        for i in range(ls):            
            for j in range(lt):                
                
                indexI, indexJ, chance = i, j, 1           
                
                while indexI < ls and indexJ < lt:

                    if s[indexI] != t[indexJ]: chance -= 1

                    if chance == 0: ans += 1
                    
                    if chance < 0: break

                    indexI += 1
                    indexJ += 1
                
        return ans