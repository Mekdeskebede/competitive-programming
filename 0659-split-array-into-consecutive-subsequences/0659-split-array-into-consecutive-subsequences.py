class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        count = defaultdict(list)
        for num in nums:
            if count[num-1]:
                length = heapq.heappop(count[num-1])
                heapq.heappush(count[num], length+1)
            else:
                heapq.heappush(count[num], 1)

        for val in count.values():
            if val and val[0] < 3:
                return False
        
        return True