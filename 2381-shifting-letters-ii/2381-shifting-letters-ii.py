class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)
        index = [0] * n
        
        for start,end,dxn in shifts:
            if dxn == 0:
                index[start] -= 1
                if end + 1 < n:
                    index[end+1] += 1
            else:
                index[start] += 1
                if end + 1 < n:
                    index[end+1] -= 1
                
        for i in range(1,n):
            index[i] += index[i-1]
        
        final_str = ""
        
        for i in range(n):
            temp = ord(s[i]) + index[i]%26
            if temp > 122:
                temp -= 26
            elif temp < 97:
                temp += 26
            final_str += chr(temp)
        
        return final_str
                    
            
                
            
        