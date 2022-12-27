class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        n = len(capacity)
        diff = []
        
        for i in range(n):
            diff.append(capacity[i] - rocks[i])
        
        diff.sort()
        j = 0
        while j < len(diff) and additionalRocks:
            additionalRocks -= diff[j]
            if additionalRocks >= 0:
                j += 1
            else:
                break
            
        return j
