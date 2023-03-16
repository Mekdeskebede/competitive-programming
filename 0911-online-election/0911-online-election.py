class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.n = len(persons)
        self.time_winner = []
        self.count = {}
        winner = (0,-1)
        
        for i in range(self.n):
            self.count[persons[i]] = self.count.get(persons[i],0) + 1
            if self.count[persons[i]] >= winner[0]:
                winner = (self.count[persons[i]],persons[i])
                self.time_winner.append((times[i],persons[i]))
            else:
                self.time_winner.append((times[i],winner[1]))
        
    def q(self, t: int) -> int:
        
        if t >= self.time_winner[-1][0]:
            return self.time_winner[-1][1]
        
        left = 0
        right = self.n - 1
        
        while left <= right:
            mid = left + (right - left)//2
            if self.time_winner[mid][0] < t:
                if self.time_winner[mid+1][0] > t:
                    print("here")
                    return self.time_winner[mid][1]
                left = mid + 1
            else:
                right = mid - 1
                
        return self.time_winner[left][1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)