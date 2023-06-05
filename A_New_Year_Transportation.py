from collections import defaultdict

n,t = map(int,input().split())
arr = list(map(int,input().split()))

for i in range(len(arr)):
    arr[i] += i

isPossible = False
t -= 1
curr = 0

while curr < len(arr):
    if curr == t:
        isPossible = True
        break
    curr = arr[curr]
    
if curr == t:
    isPossible = True

if isPossible:
    print("YES")
else:
    print("NO")
    