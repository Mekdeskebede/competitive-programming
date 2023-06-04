class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr) - 2
        while n >= 0 and arr[n] <= arr[n+1]:
            n -= 1
        if n >= 0:
            maximum = n + 1
            for j in range(maximum + 1, len(arr)):
                if arr[maximum] < arr[j] and arr[j] < arr[n]: 
                    maximum = j
            arr[maximum], arr[n] = arr[n], arr[maximum]
        return arr