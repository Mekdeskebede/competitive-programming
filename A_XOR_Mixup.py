test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    total = sum(arr)
    for num in arr:
        tempSum = total - num
        if (tempSum | num) == 0:
            print(num)
            break