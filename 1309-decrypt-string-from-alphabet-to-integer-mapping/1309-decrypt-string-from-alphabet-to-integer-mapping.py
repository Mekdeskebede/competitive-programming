class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        hashs = {}
        count = 1
        for ch in alpha:
            hashs[str(count)] = ch
            count += 1
        stack = []
        i = len(s)-1
        while i >= 0:
            if s[i] == "#":
                stack.append(s[i-2:i])
                i -= 3
            else:
                stack.append(s[i])
                i -= 1
        ans = ''
        for j in range(len(stack)-1,-1,-1):
            ans += hashs[stack[j]]
        return(ans)
        
            
            