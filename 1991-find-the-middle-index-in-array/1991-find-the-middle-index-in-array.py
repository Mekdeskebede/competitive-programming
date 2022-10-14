class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre1 = [nums[0]]
        pre2 = [nums[-1]]
        
        for i in range(1,n):
            pre1.append(pre1[-1] + nums[i])
            pre2.append(pre2[-1] + nums[-i-1])
            
        for i in range(n):
            if pre1[i] == pre2[-i-1]:
                return i
        return -1