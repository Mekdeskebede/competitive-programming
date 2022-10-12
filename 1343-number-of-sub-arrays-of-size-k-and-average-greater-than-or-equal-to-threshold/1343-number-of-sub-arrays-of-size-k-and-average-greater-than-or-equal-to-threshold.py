class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        ave = 0
        for i in range(k):
            ave += arr[i]
            
        res = 0
        prev = arr[0]
        if ave / k >= threshold :
            res += 1
        for i in range(1, len(arr)-k+1):
            ave += arr[i+k-1] - prev
            if ave/ k >= threshold:
                res += 1
            prev = arr[i]
        return res