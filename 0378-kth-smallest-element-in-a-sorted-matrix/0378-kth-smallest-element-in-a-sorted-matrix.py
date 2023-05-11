class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heapq.heapify(matrix)
        for i in range(k-1):
            small = heapq.heappop(matrix)
            if len(small) > 1:
                heapq.heappush(matrix,small[1:])

        return heapq.heappop(matrix)[0]