class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        
        if not nums or len(nums) == 1:
            return nums
        
        def reverser(nums,left, right): 
            while left < right :
                nums[left], nums[right] =  nums[right], nums[left]
                left += 1
                right -= 1
                
        k = k % len(nums)
        left = 0
        right = len(nums) - 1
        
        reverser(nums, left, right)
        reverser(nums, 0, k-1)
        reverser(nums, k , len(nums) - 1)
        