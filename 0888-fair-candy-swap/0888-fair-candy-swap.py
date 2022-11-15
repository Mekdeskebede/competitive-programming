class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(bobSizes)- sum(aliceSizes))/2
        alice = set(aliceSizes)
        
        for bob in bobSizes:
            if bob - diff in alice:
                return [int(bob - diff ) , bob]
            
