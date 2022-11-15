class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = []
        heapq.heapify(count)
        for idx,row in enumerate(mat):
            s = row.count(1)
            heapq.heappush(count,(row,idx))
        ans = []
        for _ in range(k):
            s, idx = heapq.heappop(count)
            ans.append(idx)
        return ans
        