class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        if len(nums) < 3:
            return 0
        for i in range(len(nums)-2):
            j = i +1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] >= target:
                    k -= 1
                else:
                    res += k - j
                    j += 1
        return res
                    
                
                    
                    
        