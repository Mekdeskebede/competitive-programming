class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = 0
        t = 0
        while n < len(name) and t < len(typed):
            if name[n] == typed[t]:
                if n + 1 < len(name) and name[n] == name[n+1]:
                    n += 1
                    t += 1
                else:
                    r = t + 1
                    while r < len(typed) and typed[r] == typed[t]:
                        r += 1
                    n += 1
                    t = r
            else:
                return False
        if n == len(name) and t == len(typed):
            return True
        else:
            return False
        