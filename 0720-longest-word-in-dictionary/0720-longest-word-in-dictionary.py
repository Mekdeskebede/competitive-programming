class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.insert(word)
        ans = ""
        words.sort()
        for word in words:
            temp = self.dfs(word)
            if len(ans) < len(temp):
                ans = temp
        return ans
        
    def insert(self,word):
        curr = self.root
        for char in word:
            if not curr.children[ord(char) - 97]:
                curr.children[ord(char) - 97] = TrieNode()
            curr = curr.children[ord(char) - 97]
        curr.is_end = True
    def dfs(self,word):
        curr = self.root
        for i in range(len(word)-1):
            if not curr.children[ord(word[i])-97] or not curr.children[ord(word[i])-97].is_end:
                return ""
            curr = curr.children[ord(word[i])-97]
            
        return word
                
            
                
                