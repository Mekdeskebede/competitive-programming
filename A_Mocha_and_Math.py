test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    initial = arr[0]
    for i in range(1,n):
        initial &= arr[i]
    print(initial)