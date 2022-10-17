class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        strg = str(num)
        res = 0
        beauty = strg[:k]
        
        if int(beauty) != 0 and num % int(beauty) == 0:
            res += 1
        left = 1
        for right in range(k, len(strg)):
            beauty = strg[left:right+1]
            if int(beauty) != 0 and num % int(beauty) == 0:
                res += 1
            left += 1
        return res