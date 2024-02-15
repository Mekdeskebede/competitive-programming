class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prev= 0
        ans = -1
        for num in nums:
            if num < prev:
                ans = num + prev
            prev += num
            
        return ans