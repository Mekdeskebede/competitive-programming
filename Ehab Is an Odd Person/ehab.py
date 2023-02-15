n = int(input())
arr = list(map(int, input().split()))

even = 0

for num in arr:
    if num%2 == 0:
        even += 1

if even == n or even == 0:
    print(*arr)
else:
    arr.sort()
    print(*arr)
