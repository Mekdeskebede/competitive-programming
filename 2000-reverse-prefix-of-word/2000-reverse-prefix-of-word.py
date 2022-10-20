class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
 
        word = list(word)
        idx = 0
        for i, val in enumerate(word):
            if val == ch:
                idx = i
                break
        left = 0
        right = idx
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        
        return "".join(word)