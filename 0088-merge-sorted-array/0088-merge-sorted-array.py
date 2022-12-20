class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = []
        
        p1 = 0
        p2 = 0
        
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                arr.append(nums1[p1])
                p1 += 1
            else:
                arr.append(nums2[p2])
                p2 += 1
        arr += nums1[p1:m] + nums2[p2:n]
        nums1[:] = arr[:]
                
                          
        
#         for i in range(len(nums1) - m):
#             nums1.pop()
#         for j in range(len(nums2) - n):
#             nums2.pop()
            
#         pointer = 0
#         for i in nums2:
            
#             while pointer < len(nums1) and nums1[pointer] < i:
#                 pointer += 1    
#             nums1.insert(pointer,i)

        
    