class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        modulo = 10**9+7
        best = 2**p - 2                                   
        count = 2**(p-1)-1

        return ((pow(best,count,modulo))*(best+1))%modulo