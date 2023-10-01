class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.count = 0

class MapSum:

    def __init__(self):
        self.root =TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for char in key:
            if not curr.children[ord(char)-97]:
                curr.children[ord(char)-97] = TrieNode()
                
            curr = curr.children[ord(char)-97]
        curr.is_end = True
        curr.count = val
                

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if not curr.children[ord(char)-97]:
                return 0
            curr = curr.children[ord(char)-97]
        total = 0
        def dfs(curr):
            nonlocal total
            total += curr.count
            for child in curr.children:
                if child:
                    dfs(child)
        dfs(curr)
        
        return total
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)