class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        
        left = 0
        right = n - 1
        boats = 0
        
        while left <= right:
            
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
                right -= 1
            else:
                boats += 1
                right -=1
        return boats
                
        
                
                