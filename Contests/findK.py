test = int(input())

for _ in range(test):

    n,k = map(int,input().split())
    arr = list(map(int, input().split()))

    r = n - 1
    check = False

    arr.sort()
    l = 0
    sub = 0
    while l < n-1:
        sub += arr[l]
        arr[r] -= sub
        l += 1
        if arr[r] == k:
            check = True
            break

    if check:
        print("YES")
    else:
        print("NO")

