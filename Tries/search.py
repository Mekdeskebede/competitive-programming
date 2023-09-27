class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if not curr.children[ord(char)-97]:
                return False
            curr = curr.children[ord(char)-97]
        return curr.children
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not curr.children[ord(char)-97]:
                return False
            curr = curr.children[ord(char)-97]
        return True

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.children[ord(char)-97]:
                curr.children[ord(char)-97] = TrieNode()
                
            curr = curr.children[ord(char)-97]
        curr.is_end = True    
    
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


t = Trie()
t.insert("wordsd")
t.search("words")
