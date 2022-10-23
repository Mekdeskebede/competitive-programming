class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        n = len(nums) 
        
        while odd < n:
            if nums[odd] % 2 == 0:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
            else:
                odd += 2
        return nums