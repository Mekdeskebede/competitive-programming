class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        max_time = neededTime[0]
        res = max_time

        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                res -= max_time
                max_time = 0

            current_time = neededTime[i]
            res += current_time
            max_time = max(current_time, max_time)

        return res - max_time