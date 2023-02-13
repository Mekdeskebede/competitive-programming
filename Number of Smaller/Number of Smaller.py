n, m = map(int,input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

p = 0
ans = []

for i in range(m):
    while p < n and arr1[p] < arr2[i]:
        p += 1
        
    ans.append(p)
    
print(*ans)
    