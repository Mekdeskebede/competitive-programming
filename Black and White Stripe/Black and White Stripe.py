import math

for i in range(int(input())):
    n, size = map(int, input().split())
    color = input()
    min_num = math.inf
    left = 0
    right = left + size
    while right <= n:
        temp = color[left:right].count('W')
        min_num = min(min_num,temp)
        left += 1
        right += 1

    print(min_num)
