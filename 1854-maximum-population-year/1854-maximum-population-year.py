class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0]*101
        
        for birth, death in logs:
            years[birth-1950] += 1
            years[death-1950] -= 1
        
        for i in range(1,len(years)):
            years[i] += years[i-1]
            
        max_  = [float("-inf"),None]
        for i in range(len(years)):
            if years[i] > max_[0]:
                max_ = [years[i], i+1950]
        
        return max_[1]
            