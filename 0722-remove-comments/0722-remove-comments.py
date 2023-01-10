class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        block = False
        source_code = []
        temp = ""
        
        for code in source:
            
            if not block:
                temp = ""  
            n = len(code)
            i = 0
            
            while i < len(code):
                if block:
                    if i+1 < n and code[i:i+2] == "*/":
                        block = False
                        i += 2
                        continue
                    i += 1
                    
                else:
                    if i +1 < n and code[i:i+2] == "/*":
                        block = True
                        i += 2
                        continue
                    
                    if i +1 < n and code[i:i+2] == "//":
                        break
                    
                    temp += code[i]
                    i += 1
                    
            
            if not block and temp:
                source_code.append(temp)
                temp = ""
                
        return source_code
         