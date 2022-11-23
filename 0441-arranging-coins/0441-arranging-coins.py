class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo = 1
        hi = n

        while lo <= hi:
            mid = lo+(hi-lo)//2

            if mid*(mid+1) == 2*n:
                return mid
            elif mid*(mid+1) > 2*n:
                hi = mid-1
            else:
                lo = mid+1
        return hi