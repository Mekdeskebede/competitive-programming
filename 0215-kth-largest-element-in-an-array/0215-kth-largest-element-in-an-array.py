class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.k = k
        def quickSort(arr):
            
            start = 0
            end = len(arr)
            
            if end - start <= 0:
                return start
            
            w = start + 1
            for r in range(start+1, end):
                if arr[start] > arr[r]:
                    arr[w] , arr[r] = arr[r] , arr[w]
                    w += 1
                    
            arr[start] , arr[w-1] = arr[w-1], arr[start]
            
            if end - (w-1) == self.k:
                return arr[w-1]
            elif end - (w-1) > self.k:
                return quickSort(arr[w:])
            else:
                return quickSort(arr)
        
        return quickSort(nums)
