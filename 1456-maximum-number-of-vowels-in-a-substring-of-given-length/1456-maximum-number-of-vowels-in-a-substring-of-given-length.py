class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        maxVowel = count
        for i in range(len(s) - k):
            if s[i] in vowels:
                count -= 1
            if s[i + k] in vowels:
                count += 1
            maxVowel = max(maxVowel, count)
                
        return maxVowel
                    
        
        