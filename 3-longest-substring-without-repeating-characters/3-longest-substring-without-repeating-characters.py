class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        if len(s) == 1:
            return 1

        stack = []
        res = 0
        length = len(s)
        
        for i in range(length):
            stack.append(s[i])
            pointer = i +1
            
            while pointer < length  and s[pointer] not in stack:
                stack.append(s[pointer])
                pointer += 1
                
            res = max(len(stack), res) 
            stack = []
            
        return res
            