class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        ans = 0
        num = x ^ y
        
        while num > 0:
            ans += num&1
            num >>= 1

        return ans