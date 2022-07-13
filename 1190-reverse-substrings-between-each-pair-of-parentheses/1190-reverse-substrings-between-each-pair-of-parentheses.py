class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i] =="(":
                stack.append(i)
            elif s[i] == ")":
                temp = s[stack[-1]+1:i]
                temp = temp[::-1]

                if i == len(s):
                    s[:stack[-1]-1] + temp
                else:
                    s = s[:stack[-1]+1] + temp + s[i:]

                stack.pop()
        final = ''
        for i in s:
            if i != "(" and i != ")":
                final += i
        return final
