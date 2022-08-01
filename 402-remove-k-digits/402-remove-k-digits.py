class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # if len(str)== k:
        #     return 0
        stack = []
        
        for i in num:
                
            while k > 0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
            
        
        
        stack = stack[:len(stack)-k]
          
        ans ="".join(stack)
        
        
        if ans == "" or len(num)== k:
            return "0"  
        return str(int(ans))
        
        