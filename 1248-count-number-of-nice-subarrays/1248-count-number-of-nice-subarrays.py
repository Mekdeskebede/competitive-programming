class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= 2
        d = defaultdict(int)
        d[0] = 1
        prefix = 0
        ans = 0
        for i in nums:
            prefix += i
            if(prefix - k in d):
                ans += d[prefix-k]
            d[prefix] += 1
        return ans