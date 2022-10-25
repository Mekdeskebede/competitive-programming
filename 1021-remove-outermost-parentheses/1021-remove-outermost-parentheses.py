class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        stack = []
        ans = []
        for i, val in enumerate(s):
            stack.append(val)
            if val == "(":
                count += 1
            elif val == ")":
                count -= 1
            
            if count == 0:
                ans += stack[1:-1]
                stack = []
                
        
        return "".join(ans)