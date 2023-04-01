def solve(k,arr):
    if k < 3:
        return 0
    arr = sorted(arr,reverse=True)
    sum_ = 2
    res = 0
    for i in range(len(arr)):
        sum_ += arr[i] - 1
        res += 1
        if sum_ >= k:
            return res
    return -1
        
test = int(input())
for _ in range(test):   
    k, n = map(int,input().split())
    arr = list(map(int,input().split()))

    print(solve(k,arr))
    