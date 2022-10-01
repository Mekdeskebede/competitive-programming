class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) 
        mid = n//2
        nums.sort()
        return nums[mid]