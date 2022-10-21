class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = []
        for i in score:
            temp.append(i)
        score.sort(reverse = True)
        mp = {}
        for i in range(len(temp)):
            if i == 0:
                mp[score[i]] = "Gold Medal"
            elif i == 1:
                mp[score[i]] = "Silver Medal"
            elif i == 2:
                mp[score[i]] = "Bronze Medal"
            else:
                mp[score[i]] = str(i+1)
        ans = []
        for i in temp:
            ans.append(mp[i])
        return ans