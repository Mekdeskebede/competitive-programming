class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
                    
        count_zero = 0 
        l = 0
        result = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                count_zero += 1
            
            while count_zero > k:
                if nums[l] == 0:
                    count_zero -= 1
                l += 1
            temp = r-l+1
            result = max(result, temp)
        
        return result
                