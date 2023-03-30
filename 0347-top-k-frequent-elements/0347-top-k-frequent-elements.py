class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
                
        freq_lst = []
        for i in freq:
            heapq.heappush(freq_lst, (-freq[i],i))
       
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(freq_lst)[1])
            
        return ans