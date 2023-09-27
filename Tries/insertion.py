class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.children[ord(char)-97]:
                curr.children[ord(char)-97] = TrieNode()
                
            curr = curr.children[ord(char)-97]
        curr.is_end = True
        # todo

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]