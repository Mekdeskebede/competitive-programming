class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ''
        
        first = strs[0]
        ans = len(first)
        p = 0
        for c in  first:
            for i in range(1,len(strs)):
                if p >= len(strs[i]) or strs[i][p] != c:
                    return first[:p]
            p += 1
        return first
                
                    
            