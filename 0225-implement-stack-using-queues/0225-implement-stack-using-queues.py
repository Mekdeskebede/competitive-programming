class MyStack:

    def __init__(self):
        
        self.stack = []     

    def push(self, x: int) -> None:
        
        self.stack.append(x)

    def pop(self) -> int:
        
        rmv = self.stack[-1]
        self.stack = self.stack[:len(self.stack)-1]
        return rmv

    def top(self) -> int:
        
        if self.stack:
            return self.stack[-1]

    def empty(self) -> bool:
        
        if self.stack:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()