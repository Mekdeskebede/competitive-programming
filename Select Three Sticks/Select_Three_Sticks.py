import math

test = int(input())


for i in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    
    left = 0
    right = 2
    res = math.inf
    nums.sort()
    
    while right < n:
        
        if nums[right] - nums[left] < res:
            res = nums[right] - nums[left]
        right += 1
        left += 1
    print(res)