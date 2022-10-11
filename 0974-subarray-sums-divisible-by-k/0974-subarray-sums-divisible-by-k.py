class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        total = 0
        res = 0
        
        for i in nums:
            total += i
            val = total % k
            if val in counts:
                res += counts[val]
            counts[val] += 1
            
        return res