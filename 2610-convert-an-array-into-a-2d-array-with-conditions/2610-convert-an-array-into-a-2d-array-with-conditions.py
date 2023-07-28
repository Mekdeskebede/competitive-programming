class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        freq = max(count.values())
        ans = [[] for i in range(freq)]
        i = 0
        for num, f in count.items():
            for _ in range(f):
                ans[i].append(num)
                i = (i+1)%len(ans)
        return ans 