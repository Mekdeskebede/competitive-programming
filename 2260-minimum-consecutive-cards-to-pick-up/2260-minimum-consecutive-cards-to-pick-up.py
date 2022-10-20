class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        idx = {}
        res = float('inf')
        non = res
        for i , val in enumerate(cards):
            if val in idx:
                diff = i - idx[val] + 1
                res = min(diff, res)
                idx[val] = i 
            else:
                idx[val] = i

        return -1 if res == non else res
        
        
        
        