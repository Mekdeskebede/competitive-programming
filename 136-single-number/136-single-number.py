class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        freq = Counter(nums)
        
        for idx, val in freq.items():
            if val == 1:
                return idx