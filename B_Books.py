n,t = map(int,input().split())
arr = list(map(int,input().split()))
max_ = 0
for i in range(n):
    curr = arr[i]
    if curr > t:
        continue
    j = i
    while j + 1 < n and curr + arr[j+1] <= t:
        curr += arr[j+1]
        j += 1
    max_ = max(max_,j-i+1)
print(max_)