class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda x: x[1])
        passenger = 0
        minHeap = []
        
        for i in trips:
            
            passenger += i[0]
            while minHeap and minHeap[0][0] <= i[1]:
                passenger -= minHeap[0][1]
                heapq.heappop(minHeap)
                
            if passenger > capacity:
                return False
            heapq.heappush(minHeap, (i[2], i[0]))
            
            
            
        return True