class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums.sort()
        arranged = []
        
        half = 0
        if len(nums)%2 ==0:
            half = len(nums)//2
        else:
            half =len(nums)/2 +1
        count_start =0
        count_end = half
        for i in range(half):
            
            arranged.append(nums[count_start])
            if count_end== len(nums) and len(arranged) == len(nums):
                break
                
            arranged.append(nums[count_end])
            count_start +=1
            count_end +=1
            
        return arranged
        
            
        