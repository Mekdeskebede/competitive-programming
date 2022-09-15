class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = defaultdict()
        for i in words:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        freq_lst = []
        for i in freq:
            heapq.heappush(freq_lst, (-freq[i],i))
            
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(freq_lst)[1])
            
        return ans