class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j+1] < nums[j]:
                    nums[j+1],nums[j] = nums[j],nums[j+1]
                else:
                    continue
      
        indices = []

        for indx,elt in enumerate(nums):

            if elt == target:
                indices.append(indx)
        return indices
        