class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        greater = {}
        
        for num in nums2:
            
            while stack and stack[-1] < num:
                greater[stack[-1]] = num
                stack.pop()
            stack.append(num)
            
        res = []
        for num in nums1:
            if num in greater:
                res.append(greater[num])
            else:
                res.append(-1)
                
        return res