class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        add = sum(nums[:k])
        ave = add/k
        left = 0
        for right in range(k,len(nums)):
            add += nums[right] - nums[left]
            ave = max(ave, add/k)
            left += 1
        return ave
        