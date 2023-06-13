class Solution:
    def minOperations(self, n: int) -> int:
        
        ans = 0
        for i in range(n//2,n):
            ans += (2*i+1) - n
        return ans