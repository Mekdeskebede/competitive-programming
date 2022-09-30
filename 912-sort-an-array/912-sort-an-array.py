class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        res = []
        heapq.heapify(nums)
        for i in range(len(nums)):
            res.append(heapq.heappop(nums))
        return res
            