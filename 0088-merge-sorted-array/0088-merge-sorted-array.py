class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        last = (m+n) -1
        p1 = m -1
        p2 = n-1
        
        while p1 > -1 and p2 > -1:
            
            if nums1[p1] > nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1 
            else:
                nums1[last] = nums2[p2]
                p2 -= 1
            last -= 1
            
        if p2 > -1:
            nums1[:p2+1] = nums2[:p2+1]

        
        
        
                