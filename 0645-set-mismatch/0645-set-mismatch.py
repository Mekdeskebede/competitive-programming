class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        li = []
        dup = None
        for i in nums:
            if i in li:
                dup = i
                break
            li.append(i)
        mis = None
        for i in range(len(nums)):
            if i+1 not in nums:
                mis = i+1
                break
        return [dup,mis]
                