class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        ans = [0] * n
        
        for flight in bookings:
            ans[flight[0]-1] += flight[2]
            
            if flight[1] < n:
                ans[flight[1]] -= flight[2]
        for i in range(n):
            if i != 0:
                ans[i] += ans[i-1]
                
        return ans