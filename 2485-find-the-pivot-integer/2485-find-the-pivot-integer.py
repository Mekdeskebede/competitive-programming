class Solution:
    def pivotInteger(self, n: int) -> int:
        
        if n == 1:
            return 1
        left = 0
        right = n
        left_sum = 0
        right_sum = 0
        
        while left <= right:
            if left_sum > right_sum:
                right_sum += right
                right -= 1
            elif left_sum < right_sum:
                left_sum += left
                left += 1
            else:
                left_sum += left
                left += 1
                right_sum += right
                right -= 1
                
        return left-1 if left_sum == right_sum and  left-1==right+1 else -1