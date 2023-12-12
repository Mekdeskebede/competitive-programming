class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        
        return (-heapq.heappop(heap)-1) * (-heapq.heappop(heap)-1)