n, x = map(int, input().split())
mp = {}
arr = list(map(int, input().split()))
for m in arr:
    if m in mp:
        mp[m] += 1
    else:
        mp[m] = 1

cnt = 0
for key, value in mp.items():
    m = x ^ key

    if m == key:
        y = (value - 1) * value
    else:
        y = value * mp.get(m, 0)
    
    cnt += y

print(cnt // 2)
