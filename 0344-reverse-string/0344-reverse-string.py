class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def recur(string,left, right):
            
            if left > right:
                return string
            string[left], string[right] = string[right], string[left]
            
            return recur(string, left+1,right-1)
        
        recur(s,0,len(s)-1)
            
            
            
        