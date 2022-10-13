class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        output = []
        pcnt = Counter(p)
        scnt = Counter(s[:len(p)])
        if pcnt == scnt:
            output.append(0)
            
        left = 0
        for right in range(len(p), len(s)):
            
            scnt[s[left]] -= 1   
            scnt[s[right]] = scnt.get(s[right],0) + 1
            
            if scnt[s[left]] == 0:
                scnt.pop(s[left])
            left += 1
            if pcnt == scnt:
                output.append(left)
            
                
        return output