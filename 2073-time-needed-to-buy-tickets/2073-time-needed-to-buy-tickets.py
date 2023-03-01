class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        n = len(tickets)
        time = 0
        
        while True:
            for idx in range(n):
                if tickets[idx] > 0:
                    time += 1
                    tickets[idx] -= 1
                if tickets[k] == 0:
                    return time
            