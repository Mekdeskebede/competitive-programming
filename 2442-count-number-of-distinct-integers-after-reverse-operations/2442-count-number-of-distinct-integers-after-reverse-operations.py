class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        new_nums = set(nums)
        
        for num in nums:
            new_nums.add(int(str(num)[::-1]))
            
        return len(new_nums)