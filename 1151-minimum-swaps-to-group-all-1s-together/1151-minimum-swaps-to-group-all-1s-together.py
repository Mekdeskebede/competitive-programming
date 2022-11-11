class Solution:
    def minSwaps(self, data: List[int]) -> int:
        k = data.count(1)
        zero = data[:k].count(0)
        minS = zero
        l = 0
        for r in range(k,len(data)):
            if data[r] == 0:
                zero += 1
            if data[l] == 0:
                zero -= 1
            l += 1
            minS =min(zero,minS)
        return minS