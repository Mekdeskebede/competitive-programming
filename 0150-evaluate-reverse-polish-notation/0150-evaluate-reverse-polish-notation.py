class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for token in tokens:
            if token == "*":
                mul1 = stack.pop()
                mul2 = stack.pop()
                stack.append(mul2*mul1)
                
            elif token == "+":
                sum1 = stack.pop()
                sum2 = stack.pop()
                stack.append(sum2+sum1)
                
            elif token == "-":
                sub1 = stack.pop()
                sub2 = stack.pop()
                stack.append(sub2-sub1)
            
            elif token == "/":
                div1 = stack.pop()
                div2 = stack.pop()
                if  div2%div1 != 0 and div2//div1 < 0:
                    stack.append(div2//div1+1)
                else:
                    stack.append(div2//div1)
            else:
                stack.append(int(token))
        return stack[0]