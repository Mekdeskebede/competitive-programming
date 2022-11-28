class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        while l <= h:
            mid = l + (h-l)//2
            # if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            #     return nums[mid]
            if mid%2 == 0:
                if nums[mid-1] == nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid-1] == nums[mid]:
                    l = mid + 1
                else:
                    h = mid - 1
        return nums[l-1]
