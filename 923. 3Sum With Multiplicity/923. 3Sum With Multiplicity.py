class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = {}
        res = 0
        
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                tar = target - (arr[i] + arr[j])
                res += count.get(tar,0)
            
            count[arr[i]] = count.get(arr[i], 0) + 1
        mod = (10 ** 9) + 7
        return res % mod
        