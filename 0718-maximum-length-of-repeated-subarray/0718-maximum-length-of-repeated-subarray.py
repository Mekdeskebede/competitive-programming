class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        s = "".join([chr(i) for i in nums2])
        string = ""
        res = 0
        r = 0
        while r < len(nums1):
            string += chr(nums1[r])
            if string in s:
                res = max(len(string),res)
            else:
                string = string[1:]
            r += 1
        return res
            
        