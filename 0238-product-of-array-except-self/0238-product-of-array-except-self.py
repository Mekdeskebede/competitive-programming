class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left_side = [1] *  n
        right_side = [1] * n
        ans = []
        
        for idx in range(1,n):
            left_side[idx] = left_side[idx-1] * nums[idx-1]
        
        for idx in range(1,n):
            right_side[idx] = right_side[idx-1] * nums[-idx]
            
        for i in range(n):
            ans.append(right_side[-i-1]*left_side[i])
            
        return ans