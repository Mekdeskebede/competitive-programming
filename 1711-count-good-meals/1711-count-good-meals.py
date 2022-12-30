class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        count = {}
        good = 0
        
        for food in deliciousness:
            for i in range(22):
                good += count.get(2**i - food,0)
            count[food] = 1 + count.get(food,0)
            
        return good%(10**9+7)