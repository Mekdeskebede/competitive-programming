class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        res = 0
        for left in range(len(arr)):
            res += arr[left]
            
            right = left + 2
            while right < len(arr):
                
                res += sum(arr[left:right+1])
                right += 2
        return res