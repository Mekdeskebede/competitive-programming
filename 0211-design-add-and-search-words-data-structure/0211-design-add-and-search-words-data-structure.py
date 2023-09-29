class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
         
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.children[ord(char)-97]:
                curr.children[ord(char)-97] = TrieNode()
                
            curr = curr.children[ord(char)-97]
        curr.is_end = True 

    def search(self, word: str) -> bool:
        
        def dfs(curr,i):
            for j in range(i,len(word)):

                if word[j] == ".": 
                    for child in curr.children:
                        if child and dfs(child,j+1):  
                            return True  
                    return False
                    
                else:
                    if not curr.children[ord(word[j])-97]:
                        return False
                    curr = curr.children[ord(word[j])-97]

            return curr.is_end
        
        return dfs(self.root,0)
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)