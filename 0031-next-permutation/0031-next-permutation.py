class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = n -2
        right = n -1
        
        while left >= 0:
            if nums[left] < nums[right]:
                break
            left -= 1
            right -= 1
            
        nums[right:] = sorted(nums[right:])
        for i in range(right,n):
            if nums[left] < nums[i]:
                nums[i], nums[left] = nums[left], nums[i]
                break
                
        
            
