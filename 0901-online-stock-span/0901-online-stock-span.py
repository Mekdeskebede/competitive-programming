class StockSpanner:

    def __init__(self):
        self.mon_stack = []
        self.stack = []
        self.index = 0
        
    def next(self, price: int) -> int:
        
        while self.mon_stack and self.stack[self.mon_stack[-1]] <= price:
            self.mon_stack.pop()
            
        if not self.mon_stack:
            ans = self.index + 1
        else:
            ans = self.index - self.mon_stack[-1]
            
        self.mon_stack.append(self.index)
        self.stack.append(price)
        self.index += 1
        
        return ans 
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)