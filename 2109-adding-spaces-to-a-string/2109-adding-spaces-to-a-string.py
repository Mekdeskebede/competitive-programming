class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        spaces = set(spaces)
        new_string = ""
        
        for index,char in enumerate(s):
            
            if index in spaces:
                new_string += " "
                
            new_string += char
            
        return new_string