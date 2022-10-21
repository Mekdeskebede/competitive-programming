n, l, r = map(int, input().split())
li = []
if n == 0 :
    print(0)
else :
    while n != 0 :
        li = [n%2] + li
        n //= 2
    res = 0
    for i in range(l, r+1):
        c = 0
        while i%2 == 0:
            i //= 2
            c += 1
        if li[c] == 1:
            res += 1
    print(res)