test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))

    print(sum(arr[:18]))
