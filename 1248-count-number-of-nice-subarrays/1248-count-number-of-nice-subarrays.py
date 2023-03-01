class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        for i in range(n):
            if nums[i]%2 != 0:
                nums[i] = 1
            else:
                nums[i] = 0
                
        for i in range(1,n):
            nums[i] += nums[i-1]
        
        window = defaultdict(int,{0:1})
        ans = 0
        
        for num in nums:
            if num-k in window:
                ans += window[num-k]
            window[num] += 1
            
        return ans
    
            
            
                
                
            
            
        