class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse = True)
        trainers.sort(reverse = True)
        p1 = 0
        p2 = 0
        res = 0
        while p1 < len(players) and p2 < len(trainers):
            if players[p1] <= trainers[p2]:
                res += 1
                p1 += 1
                p2 += 1
            else:
                p1 += 1
        return res
            