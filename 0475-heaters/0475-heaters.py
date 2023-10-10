class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        max_ = 0
        heaters.sort()
        for num in houses:
            low = 0
            high = len(heaters)-1
            temp = float("inf")
            
            while low < high:
                mid = (high+low)//2
                if heaters[mid] == num:
                    temp = 0
                    break
                elif heaters[mid] < num:
                    temp = min(temp,abs(heaters[mid]-num))
                    low = mid + 1
                else:
                    temp = min(temp,abs(heaters[mid]-num))
                    high = mid 
                    
            temp = min(temp,abs(heaters[low]-num))
            max_ = max(max_,temp)
                
        return max_