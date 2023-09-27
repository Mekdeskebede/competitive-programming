n, c = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
    if i == 0:
        ans += 1
    else:
        if arr[i] - arr[i-1] <= c:
            ans += 1
        else:
            ans = 1
print(ans)

