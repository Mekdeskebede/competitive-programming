class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        count = 0
        for i in range(left, right+1):
            for l, r in ranges:
                if i in [x for x in range(l, r + 1)]:
                    count += 1
                    break
        return count == right - left + 1