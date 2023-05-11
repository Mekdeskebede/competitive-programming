class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = Counter(words)
        frequency = []
        ans = []
        
        for key, val in count.items():
            frequency.append([-val,key])
            
        heapq.heapify(frequency)
        
        for i in range(k):
            word = heapq.heappop(frequency)
            ans.append(word[1])
            
        return ans