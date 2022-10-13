class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        pre = [0]
        
        for i in range(len(arr)):
            pre.append(pre[-1] ^ arr[i])
    
        res = []
        for left,right in queries:
            res.append(pre[right+1]^pre[left])

        return res