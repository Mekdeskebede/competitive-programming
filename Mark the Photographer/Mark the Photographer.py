test = int(input())

for _ in range(test):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    left = n - 1
    right = (2 * n) - 1
    while left >= 0:
        if arr[right] - arr[left] < x:
            print("NO")
            break
        left -= 1
        right -= 1
    if left < 0:
        print("YES")

