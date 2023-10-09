class TrieNode:
    
    def __init__(self):
        self.children = [None]*27
        self.weight = None

class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for i in range(len(words)):
            for j in range(len(words[i])):
                self.insert(words[i][j:]+"{"+words[i],i,len(words[i]))
        
    def insert(self,word,index,length):
        
        curr = self.root
        for char in word:
            if not curr.children[ord(char)-97]:
                curr.children[ord(char)-97] = TrieNode()
            curr = curr.children[ord(char)-97]
            curr.weight = index
        

    def f(self, pref: str, suff: str) -> int:
        search = suff + "{" + pref
        curr = self.root
        for char in search:
            if not curr.children[ord(char)-97]:
                return -1
            curr = curr.children[ord(char)-97]
            
        return curr.weight if curr.weight != None else -1
            
        
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)