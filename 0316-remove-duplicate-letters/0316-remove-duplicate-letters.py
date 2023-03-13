class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        count = Counter(s)
        seen = set()
        stack = []
        
        for char in s:
            if char in seen:
                count[char] -= 1
                continue
                
            while stack and stack[-1] > char and count[stack[-1]] > 0:
                popped = stack.pop()
                seen.remove(popped)
        
            stack.append(char)
            seen.add(char)
            count[char] -= 1
       
        return "".join(stack)