class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(bobSizes)- sum(aliceSizes))/2
        for bob in bobSizes:
            if bob - diff in aliceSizes:
                return [int(bob - diff ) , bob]
            
