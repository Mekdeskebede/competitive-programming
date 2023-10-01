class TrieNode:
    
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.count = 0

class Solution:
    
    def __init__(self):
        self.root = TrieNode()
    
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        for word in words:
            self.insert(word)
            
        ans = []
        for word in words:
            count = 0
            curr = self.root
            for i in range(len(word)):
                count += curr.count
                curr = curr.children[ord(word[i])-97]
                  
            count += curr.count
            ans.append(count)
                
        return ans     

    def insert(self,word):
        curr = self.root
        for char in word:
            if not curr.children[ord(char)-97]:
                curr.children[ord(char)-97] = TrieNode()
            curr = curr.children[ord(char)-97]
            curr.count += 1
            
       