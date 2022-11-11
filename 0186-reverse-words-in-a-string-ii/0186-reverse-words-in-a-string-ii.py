class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        l = 0
        r = 0
        while r < len(s):
            while r < len(s) and s[r] != " ":
                r += 1
            s[l:r] = s[l:r][::-1]
            l = r + 1
            r = r + 1
            