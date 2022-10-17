class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        l = 0
        first = 0
        while l < len(s):
            while l < len(s) and s[l] == " ":
                l += 1
            r  = l + 1
            while r < len(s) and s[r]!= " ":
                r += 1
            if l< len(s) and r<= len(s):
                if first == 0 :
                    ans.append(s[l:r])
                else:
                    ans.append(s[l:r] + " ")
                    
            l = r
            first += 1
        return "".join(ans[::-1])
        