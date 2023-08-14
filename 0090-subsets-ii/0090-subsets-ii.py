class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        res = []
        def backTrack(arr,index):
            ans.add(tuple(sorted(arr[:])))
            for i in range(index, len(nums)):
                arr.append(nums[i])
                backTrack(arr,i+1)
                arr.pop()
        backTrack([],0)
        for i in ans:
            res.append(list(i))
        return res