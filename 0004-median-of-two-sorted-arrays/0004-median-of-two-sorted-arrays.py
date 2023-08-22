class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = sorted(nums1 + nums2)
        if len(new_arr) % 2 != 0:
            return new_arr[len(new_arr)//2]
        return (new_arr[len(new_arr)//2] + new_arr[(len(new_arr)//2)-1] )/2
        
        
            