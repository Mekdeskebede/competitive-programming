class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        new = Counter(nums)
        
        for i, val in new.items():
            if val >= 2:
                return i
    