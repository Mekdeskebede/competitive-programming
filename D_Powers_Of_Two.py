
n, k = map(int, input().split())
if k > n:
    print("NO")
else:
    ans = []
    for i in range(32):
        if n & (1 << i):
            ans.append(1 << i)

    if len(ans) > k:
        print("NO")
    else:
        print("YES")
        i = 0
        while len(ans) < k:
            while ans[i] == 1:
                i += 1
            ans[i] //= 2
            ans.append(ans[i])
        print(*sorted(ans))
