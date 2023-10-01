class Solution:
    def longestWord(self, words: List[str]) -> str:
        longest = ""
        word_set = set(words)
        words.sort()
        for word in words:
            if len(word) > len(longest):
                isPossible = True
                for i in range(1,len(word)):
                    if word[:i] not in word_set:
                        isPossible = False
                        break
                if isPossible:
                    longest = word
        return longest
                
                