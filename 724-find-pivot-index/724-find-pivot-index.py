class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        

        sum1 = []
        sum2 = []
        j = len (nums) - 1
        for i in range(len(nums)):
            if  sum1:
                sum1.append(sum1[-1] + nums[i])
                sum2.append(sum2[-1] + nums[j])
                j -= 1
                
            else:
                sum1.append(nums[i])
                sum2.append(nums[j])
                j -= 1

        for i in range(len(nums)):
            if sum1[i] == sum2[-i-1]:
                return i
            
        return -1
        