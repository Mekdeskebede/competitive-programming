class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        count = 0
        for parentheses in s:
            if parentheses == '(':
                stack.append(count)
                count = 0
            else:
                if count < 1:
                    count = stack.pop() + 1
                else:
                    count = stack.pop() + count*2
        return count                