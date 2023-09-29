class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        for prod in products:
            self.insert(prod)
        res = []
        for i in range(len(searchWord)):
            temp = self.startsWith(searchWord[:i+1])
            res.append(temp)
        return res
    def __init__(self):
        self.root = TrieNode()

    def dfs(self,node,arr,values):
        if node.is_end:
            values.append(arr[:])
        if len(values) > 3:
            return 
        for i in range(len(node.children)):
            if node.children[i]:
                arr.append(chr(i+97)) 
                self.dfs(node.children[i],arr,values)
                arr.pop()

    def startsWith(self, prefix):
        values = []
        curr = self.root
        for char in prefix:
            if not curr.children[ord(char)-97]:
                return []
            curr = curr.children[ord(char)-97]
        arr = []
        self.dfs(curr,arr,values)
        ans = []
        i = 0
        while i < 3 and i < len(values):
            ans.append(prefix + "".join(values[i]))
            i += 1
        return ans
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.children[ord(char)-97]:
                curr.children[ord(char)-97] = TrieNode()

            curr = curr.children[ord(char)-97]
        curr.is_end = True
              
        
        