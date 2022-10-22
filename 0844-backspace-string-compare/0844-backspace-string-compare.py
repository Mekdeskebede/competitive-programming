class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        tstack = []
        sstack = []
        
        for i in s:
            if i == "#":
                if sstack:
                    sstack.pop()
            else:
                sstack.append(i)
        for i in t:
            if i == "#":
                if tstack:
                    tstack.pop()
            else:
                tstack.append(i)
        return tstack == sstack