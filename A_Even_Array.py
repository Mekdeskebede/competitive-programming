test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    step = 0
    for i in range(n):
        if (i % 2 == 0 and arr[i]%2 == 0) or (i % 2 != 0 and arr[i]%2 != 0):
            continue
        Even = arr[i] % 2
        swapped = False
        for j in range(i+1,n):
            if (j % 2 == 0 and arr[j]%2 == 0) or (j % 2 != 0 and arr[j]%2 != 0):
                continue
            if arr[i]%2 != arr[j] % 2:
                arr[i], arr[j] = arr[j], arr[i]
                step += 1
                swapped = True
                break
        if not swapped:
            step = -1
            break
    print(step)

