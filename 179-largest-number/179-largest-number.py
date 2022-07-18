class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums[0]==0 and len(set(nums))==1:
            return '0'
        for i in range(len(nums)):
            for j in range(len(nums)-1):
               
                if str(nums[i]) + str(nums[j]) > str(nums[j]) + str(nums[i]):
                    nums[i],nums[j] = nums[j],nums[i]


                else:
                    continue
                
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        return ''.join(nums)