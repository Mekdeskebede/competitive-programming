class Solution:
    def invertReverse(self,s):
        s = list(s)
        for i in range(len(s)):
            if s[i] == "1":
                s[i] = "0"
            else:
                s[i] = "1"
        s = s[::-1]
        return "".join(s)
                
    def findKthBit(self, n: int, k: int) -> str:
        
        self.binary = "0"
        def recur(n):
            if  n < 1:
                return 
            self.binary += "1" + self.invertReverse(self.binary)
            return recur(n-1)
        
        recur(n)
        return self.binary[k-1]