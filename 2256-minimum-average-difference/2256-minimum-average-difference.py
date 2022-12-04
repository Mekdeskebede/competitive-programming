class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pre = [nums[0]]
        n = len(nums)
        for i in range(n):
            if i != 0:
                pre.append(pre[-1]+nums[i])
                
        total = pre[-1]
        ans = (float('inf'),0)
    
        for idx in range(n):
            if idx!= n-1:
                ave = abs((pre[idx]//(idx+1 ))- (total-pre[idx])//(n-idx-1))
            else:
                ave = abs(pre[idx]//(idx+1))

            if ave < ans[0]:
                ans = (ave,idx)
            
        return ans[1]
        
        
                