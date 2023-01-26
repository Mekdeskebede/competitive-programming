class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        n = len(s)
        last_occurance = {s[index]:index for index in range(n)}
        
        parts = []
        last = 0
        prev = -1
        
        for i in range(n):
            
            last = max(last,last_occurance[s[i]])
            if last == i:
                parts.append(last - prev)
                prev = last 
            
        return parts
        