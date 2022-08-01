class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        idx = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[0] and popped:

                stack.pop()
                popped.pop(0)
               
                    
        return stack == []
        
        
            