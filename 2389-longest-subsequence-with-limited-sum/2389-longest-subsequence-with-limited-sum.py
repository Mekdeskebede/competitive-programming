class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        
        for i in queries:
            j = 0
            Sum = 0
            while j<len(nums):
                if Sum+nums[j] > i:
                    break 
                Sum+=nums[j]
                j+=1
            res.append(j)
        return res