class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def GCD(maximum, minimum):
            if minimum == 0:
                return maximum
            maximum , minimum = minimum,maximum%minimum
            return GCD(maximum,minimum)
        
        n = len(nums) 
        res = 0
        for i in range(n):
            prev = nums[i]
            for j in range(i,n):
                if i == j and nums[i] == k:
                    res += 1
                else:
                    prev = GCD(prev,nums[j])
                    if prev < k:
                        break
                    elif prev == k:
                        res += 1
                        
        return res
            
    