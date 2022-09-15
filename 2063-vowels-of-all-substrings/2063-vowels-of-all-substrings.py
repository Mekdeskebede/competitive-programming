class Solution:
    def countVowels(self, word: str) -> int:
        
        res = 0
        
        for i in range(len(word)):
            if word[i] in "aeiou":
                count = (len(word) - i) * (i + 1)
                res += count
        return res