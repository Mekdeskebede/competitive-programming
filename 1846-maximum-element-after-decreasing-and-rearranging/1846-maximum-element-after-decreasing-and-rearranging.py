class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        for i in range(len(arr)):
            if i == 0:
                arr[0] = 1
                continue
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1] + 1
                
        return arr[-1]
                
            