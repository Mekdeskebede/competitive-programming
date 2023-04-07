
n = int(input())
ans = 0
while n > 0:
    ans += n & 1
    n >>= 1
print(ans)