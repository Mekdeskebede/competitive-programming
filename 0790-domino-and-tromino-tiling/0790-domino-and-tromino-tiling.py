class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        elif n==2:
            return 2
        mod = 1000000007

        dp = [0]*(n+1)

        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4,n+1):
            dp[i]=(2*dp[i-1]%mod+dp[i-3]%mod)%mod
    
        return dp[n]
    
