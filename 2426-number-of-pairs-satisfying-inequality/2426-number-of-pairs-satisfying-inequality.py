class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        self.ans = 0
        def binarySearch(arr,target):
            
            low = 0
            high = len(arr) - 1
            target = target + diff
            while low <= high:
                mid = low + (high-low)//2
                if target >= arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            if low == 0 and high < 0:
                return -1
            return low
            
        def merge(left_h,right_h):
            
            for num in right_h:
                pair = binarySearch(left_h,num)
                if pair != -1:
                    self.ans += pair
                
            new = []
            left = 0
            right = 0
            while left < len(left_h) and right < len(right_h):
                if left_h[left] < right_h[right]:
                    new.append(left_h[left])
                    left += 1
                else:
                    new.append(right_h[right])
                    right += 1
            new.extend(right_h[right:])
            new.extend(left_h[left:])
            return new
        
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

            return merge(left_half, right_half)
        n = len(nums1)
        x = []
        for i in range(n):
            x.append(nums1[i] - nums2[i])
            
        mergeSort(0,n-1,x)
        
        return self.ans
            
        