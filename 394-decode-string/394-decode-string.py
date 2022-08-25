class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                temp = []
                while stack[-1] != '[':
                    temp.append(stack.pop())

                stack.pop()

                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                
                string = int(''.join(num[::-1])) * ''.join(temp[::-1])
                stack.append(string)
            
        return ''.join(stack)
                
                
                
                
            
                
        