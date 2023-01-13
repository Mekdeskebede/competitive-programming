class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        array = [float(inf)]*26
        for w in words:
            new_array = [0] * 26
            
            for char in w:
                new_array[ord(char)-97] += 1
            
            for i in range(26):
                ch = min(new_array[i], array[i])
                array[i] = ch
        
        ans = ""
        for count in range(26):
            if array[count] != 0:
                ans+=chr(count+97) * array[count]
                
        return list(ans)