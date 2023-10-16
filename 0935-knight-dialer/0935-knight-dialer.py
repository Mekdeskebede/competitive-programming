class Solution:
    def knightDialer(self, n: int) -> int:
        dp = {}
        graph = {
            0:[4,6],
            1:[8,6],
            2:[7,9],
            3:[4,8],
            4:[9,3,0],
            5:[],
            6:[1,7,0],
            7:[2,6],
            8:[1,3],
            9:[2,4]
        }
        
        def dfs(curr,pos):
            if (curr,pos) in dp:
                return dp[(curr,pos)]
            if curr == 1:
                return 1
            temp = 0
            for move in graph[pos]:
                temp += (dfs(curr-1,move)%(10**9+7))
            dp[(curr,pos)] = temp
            return dp[(curr,pos)]
        
        ans = 0
        for i in range(10):
            ans += dfs(n,i)
            
        return ans%(10**9+7)
    