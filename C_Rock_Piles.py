test = int(input())
for _ in range(test):
    n,m = map(int,input().split())
    total = abs(n - m)
    if total % 2 == 0:
        print("abdullah")
    else:
        print("hasan")