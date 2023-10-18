class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # [5,4,9] and k = 2
        # 5/2 -> [5,4,5] -> [3,4,5] = 12 
        # [5,4,9] -> [4,5,9] -> [4,5,5] -> [4,5,3]
        # k * logn
        
        max_heap = []
        heapq.heapify(max_heap)
        for pile in piles:
            heapq.heappush(max_heap,-pile)
        
        for i in range(k):
            max_ = -heapq.heappop(max_heap)
            heapq.heappush(max_heap,-(ceil(max_/2)))
        
        ans = 0
        for num in max_heap:
            ans += (-num)
        
        return ans
            
        
        
    