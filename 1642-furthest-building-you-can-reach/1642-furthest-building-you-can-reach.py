class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        heapq.heapify(heap)
        
        for i in range(len(heights)-1):
            
            if heights[i + 1] - heights[i] <= 0:
                continue
            heapq.heappush(heap,heights[i + 1] - heights[i])
            if len(heap) > ladders:
                pop = heapq.heappop(heap)
                bricks -= pop
            if bricks < 0:
                return i
        return len(heights) - 1
                
                
            
        