class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        groups = defaultdict(list)
        ans = []
        
        for i in range(len(groupSizes)):
            groups[groupSizes[i]].append(i)
            
        for key in groups:
            for i in range(0,len(groups[key]),key):
                ans.append(groups[key][i:i+key])
                
        return ans