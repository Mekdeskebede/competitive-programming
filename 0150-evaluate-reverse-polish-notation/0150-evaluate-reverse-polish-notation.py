class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num1) + int(num2)
                stack.append(result)
               
                continue
            if i == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                
                result = int(num2) // int(num1)
                if int(num2)%int(num1)!=0 and result < 0:
                    stack.append(result +1)
                else:
                    stack.append(result)
                   
                continue
            if i == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num2) - int(num1)
                stack.append(result)
                
                continue

            if i == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num2) * int(num1)
                stack.append(result)
                
                continue
            else:
                stack.append(i)

        return int(stack[0])