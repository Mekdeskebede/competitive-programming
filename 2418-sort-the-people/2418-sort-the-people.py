class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(names)
        
        for i in range(n):
            min_elt = heights[i]
            idx = i
            for j in range(i, n):
                if min_elt < heights[j]:
                    min_elt = heights[j]
                    idx = j
                    
            heights[i], heights[idx] = heights[idx],heights[i]
            names[i], names[idx] = names[idx],names[i]
                    
        return names
                           
        