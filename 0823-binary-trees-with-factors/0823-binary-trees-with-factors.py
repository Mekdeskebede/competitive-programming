class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        count = {n:1 for n in arr}
        arr.sort()
        for i in range(1,len(arr)):
            for j in range(i):
                if arr[i]/arr[j] in count:
                    count[arr[i]] += count[arr[i]/arr[j]] * count[arr[j]]
            
        return sum(count.values())%(10**9+7)