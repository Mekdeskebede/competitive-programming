test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    check = []

    for val in arr:
        if val in check:
            print("NO")
            break
        else:
            check.append(val)
    if len(check) == len(arr):
        print("YES")