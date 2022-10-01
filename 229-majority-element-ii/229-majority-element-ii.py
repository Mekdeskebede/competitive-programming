class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res = []
        freq = Counter(nums)
        
        for key in freq:
            if freq[key] > len(nums) / 3:
                res.append(key)
                
        return res