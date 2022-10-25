class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for i in s:

            if i.isupper():
                if stack and stack[-1].islower() and stack[-1].upper() == i:
                    stack.pop()
                else:
                    stack.append(i)
                
            elif i.islower():
                if stack and stack[-1].isupper() and stack[-1].lower() == i:
                    stack.pop()
                else:
                    stack.append(i)
                    
        return "".join(stack)