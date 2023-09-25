class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        mini = prices[0]
        for i in range(1,len(prices)):
            profit = max(profit, prices[i] - mini)
            mini = min(mini, prices[i])
            
        return profit