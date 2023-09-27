test = int(input())
for _ in range(test):
    n = int(input())
    arr = [ i for i in range(1,n+1)]
    # print(arr)
    arr[:] = arr[::-1]
    flag = True
    if n%2 == 0:
        arr[:n//2] = arr[:n//2][::-1]
    else:
        arr[:n//2+1] = arr[:n//2+1][::-1]
    # print(arr)
    for i in range(0,n):
        if i == 0:
            if abs(arr[i]-arr[i+1]) != 1:
                flag = False
                break
        elif i == n-1:
            if abs(arr[i]-arr[i-1]) != 1:
                flag = False
                break
        elif abs(arr[i]-arr[i-1]) != 1 and abs(arr[i]-arr[i+1]) != 1:
            flag = False
            break
    if flag:
        print(*arr)
    else:
        print(-1)
