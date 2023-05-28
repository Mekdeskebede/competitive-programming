class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count = [0] * 7
        pointer = 0
        for i in range(len(columnTitle) -1, -1, -1):
            count[i] = (ord(columnTitle[i]) - ord('A') + 1) * 26 ** pointer
            pointer += 1
        return sum(count)