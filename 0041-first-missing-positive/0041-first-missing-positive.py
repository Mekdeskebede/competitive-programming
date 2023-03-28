class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for i in range(n):
            while i+1 != nums[i]:
                if nums[i] <= 0 or nums[i] > n:
                    break
                temp = nums[i] - 1
                if nums[i] == nums[temp]:
                    break
                nums[i], nums[temp] = nums[temp], nums[i]
                
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n + 1