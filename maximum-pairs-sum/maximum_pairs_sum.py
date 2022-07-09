def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # nums = nums
    operation = 0
        
    for i in range(len(nums)):
        
        for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j]==k  and nums[i] != k and nums[j] != k:
                        
                        nums[i]=0
                        nums[j]=0
                        operation += 1
                    
    return operation