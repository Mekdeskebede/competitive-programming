class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0,prices[0]]]
        
        for i in range(1,len(prices)):
            curr_profit = max(dp[-1][0], prices[i] - dp[-1][1] - fee)
            buy = min(dp[-1][1], prices[i] - curr_profit)
            dp.append([curr_profit, buy])
            
        return dp[-1][0]