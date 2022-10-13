class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        pre = sum(chalk)
        
        k = k % pre
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]
            
        
            
            