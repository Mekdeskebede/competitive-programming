class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        maps = {")":"(", "]":"[", "}" :"{" }
        
        for char in s:
    
            if stack and char in maps and maps[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return not stack
                
            
            
            
            