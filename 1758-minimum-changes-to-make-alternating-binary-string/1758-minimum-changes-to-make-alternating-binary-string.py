class Solution:
    def minOperations(self, s: str) -> int:
        s1 = 1
        step1 = 0
        s2 = 0
        step2 = 0
        for b in s:
            if 1-s1 != int(b):
                step1 += 1
            s1 = 1 - s1
                
            if 1-s2 != int(b):
                step2 += 1
            s2 = 1 - s2
            
        return min(step1, step2)