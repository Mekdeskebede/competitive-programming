class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = len(s2)
        k = len(s1)
        
        if k > n:
            return False
        
        s1_count = Counter(s1)
        s2_count = Counter(s2[:k])
        
        if s1_count == s2_count:
            return True
        
        left = 0
        for right in range(k,n):
            
            s2_count[s2[right]] += 1
            
            s2_count[s2[left]] -= 1
            if s2_count[s2[left]] ==0:
                del s2_count[s2[left]]
            left += 1
            
            if s1_count == s2_count:
                return True
            
        return False
        