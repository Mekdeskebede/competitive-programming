for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    left = 1
    right = n - 1

    while left < right:
        if sum(nums[:left+1]) < sum(nums[right:]):
            print("YES")
            break
        else:
            left += 1
            right -= 1
    if left >= right:
        print("NO")

