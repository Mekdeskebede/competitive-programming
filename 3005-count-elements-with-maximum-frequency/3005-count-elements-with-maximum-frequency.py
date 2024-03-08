class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        values = list(count.values()) 
        max_freq = max(values)
        ans = values.count(max_freq) * max_freq
        
        return ans