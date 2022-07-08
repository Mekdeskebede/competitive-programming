
def rearrangeArray(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(nums)-1):
            if (nums[i-1] + nums[i+1]) / 2 == nums[i]:
                for j in nums[i:]:
    
                    if (nums[i-1] + j) / 2 != nums[i]:
                        
                        nums[i+1],nums[nums.index(j)] = nums[nums.index(j)],nums[i+1]
                        break
        return nums
    
    
print(rearrangeArray([3,2,1]))  