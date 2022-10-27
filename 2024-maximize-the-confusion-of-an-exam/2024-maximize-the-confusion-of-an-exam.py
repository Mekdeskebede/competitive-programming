class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        d = {"T":0, "F":0}
        
        length = 0
        l = 0
        r = 0
        while r < len(answerKey):
            d[answerKey[r]] += 1
            
            while d["T"] > k and d["F"] > k:
                d[answerKey[l]] -= 1
                l += 1
            length = max(r - l + 1, length)
            r += 1
        return length
    