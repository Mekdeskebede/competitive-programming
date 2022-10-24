class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        d = Counter(arr)
        li = list(d.values())
        li.sort(reverse = True)
        initial = len(arr)
        target = len(arr)/2
        res = 0
        for i in li:
            if initial > target:
                initial -= i
                res += 1
            else:
                break
        return res