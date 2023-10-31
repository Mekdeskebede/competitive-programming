class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4300:
            return 1
        dp = {}

        def dfs(a,b):
            if (a,b) in dp:
                return dp[(a,b)]
            if b <= 0 and a <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            
            dp[(a,b)] = 0.25 * (dfs(a-100,b) + dfs(a-75,b-25) + dfs(a-50,b-50) + dfs(a-25,b-75))
            return dp[(a,b)]
        
        return dfs(n,n)