class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1]
        
        for i in range(len(nums)-1):
            ans.append(ans[-1] * nums[i])
          
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= temp
            temp *= nums[i]
            
        return ans