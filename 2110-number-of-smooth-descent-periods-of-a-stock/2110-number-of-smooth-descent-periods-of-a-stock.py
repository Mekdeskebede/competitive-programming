class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        Price = None
        count = 0
        again = 0
        
        for i in prices:
            if Price and Price - i == 1:
                count += 1 + again
                again += 1
            else:
                again = 0
                
            count += 1
            Price = i
            
        return count
        