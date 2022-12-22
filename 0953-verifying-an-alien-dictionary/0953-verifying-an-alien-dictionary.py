class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        alien = {}
        
        count = 0
        for char in order:
            alien[char] = count
            count += 1
            
        value = []
        for i in range(len(words)):
            val = []
            for j in words[i]:
                val.append(alien[j])
            value.append(val)
        prev = value[0]
        for v in value:
            if prev > v:
                return False
            prev = v
        return True
                        
                    
                    
            