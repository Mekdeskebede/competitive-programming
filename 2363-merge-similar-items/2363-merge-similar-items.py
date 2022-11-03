class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        ret = {}
        for val, weight in items1:
            ret[val] = ret.get(val,0) + weight
        
        for val, weight in items2:
            ret[val] = ret.get(val,0) + weight
        
        res = []
        for val, weight in ret.items():
            res.append([val,weight])
        
        res.sort()
        
        return res