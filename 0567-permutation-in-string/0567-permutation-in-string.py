class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1Count = Counter(s1)
        s2Count = Counter(s2[:n])
        
        if s1Count == s2Count:
            return True
        left = 0
        for right in range(n,len(s2)):
            s2Count[s2[left]] -= 1
            s2Count[s2[right]] = 1 + s2Count.get(s2[right], 0)
            if s2Count[s2[left]] == 0:
                s2Count.pop(s2[left])
            if s1Count == s2Count:
                return True
            left += 1
            
        return False