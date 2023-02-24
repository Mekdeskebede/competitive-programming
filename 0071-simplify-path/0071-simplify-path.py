class Solution:
    def simplifyPath(self, path: str) -> str:
        
        paths = path.split("/")
        stack = []
        
        for path in paths:
            if stack and path =="..":
                stack.pop()
            elif path == "." or path == "" or path == "..":
                continue
            else:
                stack.append(path)
        
        res = ""
        if stack:
            res = "/".join(stack)
        
        return "/" + res
                