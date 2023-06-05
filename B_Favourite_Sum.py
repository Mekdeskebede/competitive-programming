test = int(input())

for _ in range(test):
    n,x = map(int,input().split())
    favourite = list(map(int,input().split()))

    total = (x * (x+1))/2
    for i in range(n):
        if favourite[i] < x:
            total -= ( 2 * favourite[i])
    print(total)