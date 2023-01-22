class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        if n == 0:
            return [[]]
        for i in range(1, n + 1):
            if s[:i] != s[:i][::-1]:
                continue
            cur = self.partition(s[i:])
            for j in range(len(cur)):
                res.append([s[:i]] + cur[j])
        return res