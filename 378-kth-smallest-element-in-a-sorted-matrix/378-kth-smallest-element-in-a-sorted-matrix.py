class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        new_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_list.append(matrix[i][j])
                
        heapq.heapify(new_list)
        
        for i in range(k-1):
            heapq.heappop(new_list)
        return new_list[0]

        
        