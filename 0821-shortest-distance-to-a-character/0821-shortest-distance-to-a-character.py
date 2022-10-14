class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        pos = -n
        res = [0]*(n)
        for i in range(n):
            if s[i] == c:
                pos = i
            res[i] = i - pos  
        for j in range(n-1,-1,-1):
            if s[j] == c:
                pos = j
            res[j] = min(res[j] , abs(j-pos))
            
        return res