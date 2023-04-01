test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))

    k = sum(arr)/n

    count = 0
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if (arr[i] + arr[j])/2 == k:
    #             count += 1

    d = {}
    for num in arr:
        if 2 * k - num in d:
            count += d[2 * k - num]
        d[num] = 1 + d.get(num,0)
    print(count)




    