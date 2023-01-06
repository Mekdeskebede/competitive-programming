class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        n = len(costs)
        costs.sort()
        bar = 0
        i = 0
        
        while i < n:
            if costs[i] <= coins:
                bar += 1
                coins -= costs[i]
                i += 1
            else:
                break
                
        return bar