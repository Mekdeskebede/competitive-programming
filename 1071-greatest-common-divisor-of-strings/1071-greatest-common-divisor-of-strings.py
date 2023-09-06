class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        n = len(str1)
        m = len(str2)
        prefix = 0
        i = 0
        while i < n and i < m:
            if str1[i] == str2[i]:
                prefix = i
                i += 1
            else:
                break
                
        for i in range(prefix,-1,-1):
            if (n) % (i +1) == 0 and (m) % (i +1) == 0:
                pre = str1[:i+1]
                if pre * (n//(i+1)) == str1 and pre * (m//(i+1)) == str2:
                    return pre
                
        return ""
        