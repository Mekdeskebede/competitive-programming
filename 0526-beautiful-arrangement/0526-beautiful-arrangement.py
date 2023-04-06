class Solution:
    def countArrangement(self, n: int) -> int:
        
        self.count = 0
        seen = set()
        
        def permutation(num):
            
            if num == n+1:
                self.count += 1
                return
            
            for i in range(1, n+1):
                if num % i != 0 and i % num != 0:
                    continue
                if i not in seen:
                    seen.add(i)
                    permutation(num+1)
                    seen.remove(i)

        permutation(1)
        
        return self.count
