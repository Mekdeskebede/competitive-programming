class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i,currSum):
            if (i,currSum) in dp:
                return dp[(i,currSum)]
            if i == len(coins) or currSum > amount:
                return 0
            if currSum == amount:
                return 1
           
            dp[(i,currSum)] = dfs(i,currSum+coins[i]) + dfs(i+1,currSum)
            
            return dp[(i,currSum)]
            
        return dfs(0,0)