class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = {}
        letters = {}
        l = 0
        r = 0
        res = 0
        while r < len(s):
            count[s[r]] = count.get(s[r],0) + 1
            if r - l + 1 < minSize:
                r += 1
            else:
                if len(count) <= maxLetters:
                    letters[s[l:r+1]] = letters.get(s[l:r+1], 0) + 1
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                r += 1
                l += 1
        return max(letters.values()) if letters else 0
                    