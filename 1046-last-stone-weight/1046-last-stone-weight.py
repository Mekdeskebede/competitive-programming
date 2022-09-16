class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        new_list = []
        heapq.heapify(new_list)
        for i in stones:
            heapq.heappush(new_list, -i)
            
        while len(new_list) > 1:
            x = heapq.heappop(new_list)
            y = heapq.heappop(new_list)
            
            if x == y:
                continue
            elif x > y:
                heapq.heappush(new_list, y - x)
            else:
                heapq.heappush(new_list, x - y)
        
        return -new_list[0] if new_list else 0
            
            
            
            