class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        step = 0
        
        for char in s_count:
            if char not in t_count:
                step += s_count[char]
            elif s_count[char] > t_count[char]:
                step += s_count[char] - t_count[char]
        return step