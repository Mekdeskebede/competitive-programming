class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def recur(k):
            if k == 1:
                return 0
            mid = recur((k+1)//2)
            
            if k % 2 == 0:
                if mid == 0:
                    return 1
                return 0
            
            return mid
        
        return recur(k)