class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        target = math.ceil(totalSum/2)
        dp = {}
        def BackTrack(index,currSum):
            nonlocal target
            if currSum >= target or index >= len(stones):
                return abs(currSum - (totalSum-currSum))
            
            if (index,currSum) not in dp:
                dp[(index,currSum)] = min(BackTrack(index+1,currSum),BackTrack(index+1,currSum+stones[index]))
            return dp[(index,currSum)]
        
        return BackTrack(0,0)