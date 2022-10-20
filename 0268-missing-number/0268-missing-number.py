class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
            
#         l = 0
#         r = len(nums)
        
#         while l < r:
#             mid = (l + r) // 2
            
#             if mid == nums[mid]:
#                 l = mid
#             else:
#                 r = mid
#         return nums[mid]
        
        
        
        