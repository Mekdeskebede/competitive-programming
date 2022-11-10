class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if stack:
                if ch == stack[-1][0]:
                    stack[-1][1] += 1
                else:
                    stack.append([ch,1])
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch,1])
        res = ""

        for ch, i in stack:
            res += ch * i
        return res
            