class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        max_ = 0
        n = len(satisfaction)
        
        for i in range(n):
            curr = satisfaction[i] 
            for j in range(i+1, n):
                curr += satisfaction[j] * (j-i+1)
            max_ = max(max_, curr)
        
        return max_
                
            
            
        