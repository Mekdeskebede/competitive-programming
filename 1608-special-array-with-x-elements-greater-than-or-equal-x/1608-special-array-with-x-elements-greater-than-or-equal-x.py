class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l = 0 
        h = len(nums) - 1
        while l <= h:
            mid = l + (h - l) // 2
            x = len(nums) - mid
            if nums[mid] >= x:
                if mid == 0 or nums[mid - 1] < x:
                    return x
                else:
                    h = mid - 1
            else:
                l = mid + 1
        return -1
        