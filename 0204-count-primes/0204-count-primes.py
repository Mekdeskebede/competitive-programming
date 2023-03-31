class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2:
            return 0
        
        prime_nums = [True] * (n)
        prime_nums[0] = prime_nums[1] = False
        i = 2
        
        while i * i < n:
            if prime_nums[i]:
                j = i * i
                while j < n:
                    prime_nums[j] = False
                    j += i
            i += 1
        
        count = prime_nums.count(True)
        
        return count
        