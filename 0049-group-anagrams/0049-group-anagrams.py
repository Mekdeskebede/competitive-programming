class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        
        for s in strs:
            temp = "".join(sorted(s))
            if temp in groups:
                groups[temp].append(s)
            else:
                groups[temp] = [s]
        return groups.values()