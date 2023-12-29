class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n : return -1
        if d == n : return sum(jobDifficulty)

        @cache
        def dp(i , days , max_) :
            if i == n and days == 0: return 0
            if i == n or days == 0: return 9e9
            max_ = max(max_, jobDifficulty[i]) 
            return min(max_ + dp(i + 1, days - 1, 0), dp(i + 1, days, max_))
        
        return dp(0, d, 0)