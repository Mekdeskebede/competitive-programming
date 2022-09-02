class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l_ptr = 0
        r_ptr= len(people) -1
        boats = 0
        
        while l_ptr <= r_ptr:
            if people[r_ptr] + people[l_ptr] <= limit:
                l_ptr += 1
                r_ptr -= 1
                boats +=1
            else:
                r_ptr -= 1
                boats +=1
        return boats
                
                
                