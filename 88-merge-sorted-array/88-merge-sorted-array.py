class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
#         right = len(nums1) - 1
        
#         for i in nums2:
            
#             while 
        
        for i in range(len(nums1) - m):
            nums1.pop()
        for j in range(len(nums2) - n):
            nums2.pop()
            
        pointer = 0
        for i in nums2:
            
            while pointer < len(nums1) and nums1[pointer] < i:
                pointer += 1
                
            nums1.insert(pointer,i)

        
    