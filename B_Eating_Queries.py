test = int(input())
def binary(target,nums):
    
    left = 0
    right = len(nums) - 1
    if target > nums[right]:
        return -1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left + 1
    
for _ in range(test):
    n, q = map(int,input().split())
    sugar = list(map(int,input().split()))
    sugar.sort(reverse=True)
    for i in range(1,n):
        sugar[i] += sugar[i-1]
    
    for _ in range(q):
        query = int(input())
        print(binary(query,sugar))