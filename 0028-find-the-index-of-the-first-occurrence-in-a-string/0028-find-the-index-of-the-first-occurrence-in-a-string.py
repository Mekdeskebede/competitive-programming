class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            temp = i
            for j in range(len(needle)):
                if temp < len(haystack) and haystack[temp] == needle[j]:
                    j += 1
                    temp +=1 
                else:
                    break
            if j == len(needle):
                return i
        return -1
        