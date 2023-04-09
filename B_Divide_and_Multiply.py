test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    last_odd = n-1
    for i in range(n-1,-1,-1):
        if arr[i] % 2 != 0:
            last_odd = i
            break
    
    for i in range(n):
        if i == last_odd:
            continue
        while arr[i]%2==0:
            arr[i] //= 2
            arr[last_odd] *= 2

    print(sum(arr))
