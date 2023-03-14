class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        modulo = 10**9+7
        res = 0
        stack = []
        curr_sum = 0
        for i in range(len(arr)):
            min_count = 1
            while stack and stack[-1][0] >= arr[i]:
                val, count = stack.pop()
                min_count += count
                curr_sum -= val * count
                
            curr_sum += arr[i] * min_count
            res += curr_sum
            stack.append((arr[i],min_count))
                
        return res%modulo