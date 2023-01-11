class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        lis = list(i for i in range(1,n+1))
        n = len(lis)
        idx = 0
        
        while len(lis) > 1:
            
            n = len(lis)
            idx = (idx + k-1) % n
            lis.pop(idx)
            
        return lis[0]
            
            
            
        