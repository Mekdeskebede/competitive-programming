class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ["a", "e", "i", "o", "u"]
        s =[i for i in s]
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].lower() in vowels and s[r].lower() in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l].lower() in vowels:
                r -= 1
            elif s[r].lower() in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(s)