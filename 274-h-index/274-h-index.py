class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        i = 1
        
        while i <= len(citations):
            if citations[len(citations)-(i)] < i:
                break
            i += 1
        return i-1