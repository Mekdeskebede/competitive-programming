class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack1 = []
        
        for char in s:
            if char == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(char)
                
        stack2 = []
        
        for char in t:
            if char == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(char)
        
        return "".join(stack1) == "".join(stack2)