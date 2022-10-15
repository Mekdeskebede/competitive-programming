test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = n

    left = 0
    right = 1
    while right < n:
        if arr[left] == arr[right]:
            res -= 2
            right += 2
            left += 2
        else:
            left += 1
            right += 1
    print(res)

