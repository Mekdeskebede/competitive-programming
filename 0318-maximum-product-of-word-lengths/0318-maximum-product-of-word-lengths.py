class Solution:
    def maxProduct(self, words: List[str]) -> int:
        unique = []
        maximum = float('-inf')
        
        for word in words:
            unique.append(set(word))
        
        for i in range(len(unique)):
            for j in range(i+1,len(unique)):
                if not (unique[i] & unique[j]):
                    maximum = max(maximum,len(words[i])*len(words[j]))
                    
        return maximum if maximum != float('-inf') else 0
