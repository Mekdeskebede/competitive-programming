class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        greater_list = []
        for elts in nums1:
            greater = -1
            if elts == nums2[-1]:
                greater_list.append(greater)
                continue
            else:
                temp = nums2[nums2.index(elts)+1:]
                print(temp)
            for num in temp:
                if num > elts:
                    greater = num
                    break
            greater_list.append(greater)
        return greater_list
                