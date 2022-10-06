class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for i in path:
            if i == "." or i == "":
                continue
            elif i == ".." and stack:
                stack.pop()
            elif i == "..":
                continue
            else:
                stack.append(i)
        return "/"+"/".join(stack) 
                
            
                
            
        
        