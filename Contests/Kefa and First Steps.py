n = int(input())

nums = list(map(int,input().split()))


def maxSize(nums):
    max_size = 0
    if n <= 1:
        return n
    left = 0
    right = 1

    while right < n:

        if nums[right] < nums[right-1]:
            left = right
            right += 1
        else:
            right += 1
        max_size = max(max_size, right-left)
    return max_size

print(maxSize(nums))
