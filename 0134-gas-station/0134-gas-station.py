class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = []
        for i in range(len(gas)):
            ans.append(gas[i]-cost[i])
            
        if sum(ans) < 0:
            return -1
            
        curr = 0
        p = 0
        p2 = 0
        while p < len(ans):
            curr += ans[p]
            if curr < 0:
                p2 = p+1
                curr = 0
            p += 1
            
        return p2
        
        
            
        
        