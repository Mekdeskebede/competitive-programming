class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        n = len(s)
        m = len(p)
        
        if m > n :
            return []
        
        p_hash = Counter(p)
        anagram = []
        window = Counter(s[:m])
        
        if window == p_hash:
                anagram.append(0)
        
        left = 0
        for right in range(m,n):
            
            window[s[left]] -= 1
            
            if window[s[left]] == 0:
                window.pop(s[left])
                
            left += 1 
            
            window[s[right]] = 1 + window.get(s[right],0)
            
            
            if window == p_hash:
                anagram.append(left)
        
        return anagram
                