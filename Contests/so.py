n = int(input())

arr = list(map(int, input().split()))

arr.sort()

sum1= sum(arr[:n])

sum2 = sum(arr[n:])

if sum1 != sum2:
    print(*arr)
else:
    print(-1)

