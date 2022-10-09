class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maps = {0: -1}
        max_len = 0
        count = 0
        for idx, val in enumerate(nums):
            if val == 1:
                count += 1
            else:
                count -= 1
            
            if count in maps:
                max_len = max(max_len, idx - maps[count])
            else: 
                maps[count] = idx
        return max_len