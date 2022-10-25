class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        d = {}
        for i in range(len(names)):
            d[heights[i]] = names[i]
        heights.sort(reverse = True)
        
        res = []
        for i in heights:
            res.append(d[i])
            
        return res
        
        