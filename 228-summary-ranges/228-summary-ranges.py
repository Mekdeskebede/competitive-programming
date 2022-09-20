class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        
        left = 0
        right = 0
        res = []

        while left <= right < len(nums):
            if len(nums) - right > 1 and nums[right + 1] - nums[right] == 1:
                right = right + 1
            else:
                if left == right:
                    res.append(str(nums[left]))
                else:
                    res.append(str(nums[left]) + "->" + str(nums[right]))
                right += 1
                left = right

        return res