class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        n = len(trips)
        last = 0
        
        for i in range(n):
            last = max(last,trips[i][2])
        
        line = [0] * (last+1)
        for num, start, end in trips:
            line[start] += num
            if end+1 < last+1:
                line[end] -= num
        
        for i in range(1,last+1):
            line[i] += line[i-1]
        
        for people in line:
            if people > capacity:
                return False
            
        return True
            