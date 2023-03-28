class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.ans = [0] * n
        nums = [[nums[i],i] for i in range(n)]
        def binarySearch(arr,target):
            low = 0
            high = len(arr) - 1
    
            while low <= high:
                mid = low + (high-low)//2
                if target > arr[mid][0]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            if low == 0 and high < 0:
                return 0
            return low
        
        def merge(left_arr,right_arr):
            
            for target in left_arr:
                less = binarySearch(right_arr,target[0])
                self.ans[target[1]] += less
                
            new = []
            left = 0
            right = 0
            
            while left < len(left_arr) and right < len(right_arr):
                if left_arr[left] < right_arr[right]:
                    new.append(left_arr[left])
                    left += 1
                else:
                    new.append(right_arr[right])
                    right += 1
                    
            new.extend(right_arr[right:])
            new.extend(left_arr[left:])
            return new
        
        def mergedSort(left,right,arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergedSort(left, mid, arr)
            right_half = mergedSort(mid + 1, right, arr)
            
            return merge(left_half,right_half)
        
        mergedSort(0,len(nums)-1,nums)
        return self.ans
            
            