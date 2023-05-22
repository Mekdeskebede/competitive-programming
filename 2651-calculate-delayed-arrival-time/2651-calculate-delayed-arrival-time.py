class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        total = arrivalTime + delayedTime
        if total < 24:
            return total
        else:
            return total - 24
        