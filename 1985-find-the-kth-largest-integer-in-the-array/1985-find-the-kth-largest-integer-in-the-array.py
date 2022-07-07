class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums2 = []
        for i in nums:
            nums2.append(int(i))
        nums2 = sorted(nums2)
        nums2.reverse()
        

        
        return str(nums2[k-1])
        