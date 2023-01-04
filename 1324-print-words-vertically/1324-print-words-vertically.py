class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        s = s.split(" ")
        n = len(s)
        maxi = 0
        
        for word in s:
            maxi = max(maxi,len(word))
            
        output = []
        for col in range(maxi):
            temp = ""
            
            for row in range(len(s)):
                if col < len(s[row]):
                    temp += s[row][col]
                else:
                    temp += " " 
                    
            output.append(temp.rstrip())
            
        return output
                    
        
        