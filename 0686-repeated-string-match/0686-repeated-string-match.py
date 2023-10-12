class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(a)
        m = len(b)
        
        LPS = [0 for _ in range(m)]
        j = 0
        i = 1
        while i < m:
            if b[j] == b[i]:
                LPS[i] = j + 1
                j += 1
                i += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = LPS[j - 1]
                    
        i = 0
        j = 0
        while i < n + m:
            if b[j] == a[i%n]:
                if j == m-1:
                    return ceil((i+1) / n)
                i += 1
                j += 1
            elif j > 0:
                j = LPS[j-1]
            else:
                i += 1
                
        return -1
        