class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        h = len(arr) - 1
        
        while l <= h:
            mid = l + (h-l)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid+1]:
                h = mid - 1
            else:
                l = mid + 1
                