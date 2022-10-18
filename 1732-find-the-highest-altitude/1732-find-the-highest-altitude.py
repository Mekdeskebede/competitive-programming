class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        sum = 0
        for i in gain:
            sum += i
            res = max(res,sum)
                
        return res