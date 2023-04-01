n , enemy = map(int,input().split())

players = list(map(int, input().split()))

players.sort()

left = 0
right = n - 1
count = 1
res = 0
while left <= right:
    if ( players[right] * count) > enemy:
        count = 1
        res += 1
        right -= 1
    else:
        count += 1
        left += 1
print(res)

