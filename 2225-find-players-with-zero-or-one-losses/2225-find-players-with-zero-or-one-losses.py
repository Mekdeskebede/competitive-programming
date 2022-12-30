class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        matches_dict = defaultdict()
        
        for win, lost in matches:
            
            if win not in matches_dict:
                matches_dict[win] = 0
                
            matches_dict[lost] = matches_dict.get(lost,0) - 1 
        
        win = []
        oneLost = []
        for key, val in matches_dict.items():
            if val == 0:
                win.append(key)
            elif val == -1:
                oneLost.append(key)
                
        win.sort()
        oneLost.sort()
        
        return [win, oneLost]