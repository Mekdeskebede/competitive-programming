class Solution:
    def decodeString(self, s: str) -> str :
        
        stack = []
        def recur(stack,s,ptr):

            if ptr >= len(s):
                return stack

            if s[ptr] != "]":
                stack.append(s[ptr])
            
            elif s[ptr] == "]":
                
                string = ""
                temp = len(stack) -1
                while temp >= 0 and stack and stack[temp] != "[":
                    string = stack.pop() + string
                    temp -= 1
                    
                num = ""
                stack.pop()
                temp -= 1
                while stack and stack[temp].isdigit():
                    num = stack.pop() +num
                    temp -= 1
    
                stack.append(int(num)*string)
                    
            recur(stack,s,ptr+1) 
            
        recur(stack,s,0)
        
        
        ans = "".join(stack)
        
        return "" if ans.isdigit() else ans
         
        
        