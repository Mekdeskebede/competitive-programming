class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        while k and numOnes:
            ans += 1
            k -= 1
            numOnes -= 1
            
        while k and numZeros:
            k -= 1
            numZeros -= 1
            
        while k and numNegOnes:
            ans -= 1
            k -= 1
            numNegOnes -= 1
            
        return ans
        