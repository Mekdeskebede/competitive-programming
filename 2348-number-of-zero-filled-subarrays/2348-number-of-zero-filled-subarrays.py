class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        ans = 0
        zero = 0
        
        for num in nums:
            if num==0:
                zero+=1
            else:
                ans += (zero*(zero+1))//2
                zero = 0
                
        if zero:
            ans += (zero*(zero+1))//2
            
        return ans