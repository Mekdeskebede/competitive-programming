class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
    
        n = len(piles)
        heap = []
        heapq.heapify(heap)
        
        for num in piles:
            heapq.heappush(heap,-num)
            
        for i in range(k):
            num = heapq.heappop(heap)
            heapq.heappush(heap, -math.ceil((-num)/2))
           
        total = 0
        for num in heap:
            total += (-num)
            
        return total