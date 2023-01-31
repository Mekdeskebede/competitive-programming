class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        res = sorted(zip(ages,scores))
        dp = [i[1] for i in res]

        for i in range(1,len(res)):
            for j in range(i):
                if res[i][1] >= res[j][1]:
                    dp[i] = max(dp[i],dp[j]+res[i][1])

        return max(dp)