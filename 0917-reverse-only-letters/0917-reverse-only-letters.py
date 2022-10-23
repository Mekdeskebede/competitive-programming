class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        li = list(s)
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].isalpha() and s[r].isalpha():
                li[l], li[r] = li[r], li[l]
                l += 1
                r -= 1
            elif not s[l].isalpha() and not s[r].isalpha():
                l += 1
                r -= 1
            elif not s[l].isalpha():
                l += 1
            else:
                r -= 1
        return "".join(li)
                