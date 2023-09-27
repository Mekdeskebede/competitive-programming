def solve(n,s,arr):
    big = None
    curr = 0
    for i in range(n):
        curr += arr[i]
        if big == None:
            big = i
        else:
            if arr[big] < arr[i]:
                big = i
        if curr > s:
            return big + 1
    return 0

test = int(input())
for _ in range(test):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n,s,arr))