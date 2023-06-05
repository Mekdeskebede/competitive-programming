test = int(input())
for _ in range(test):
    left, right = map(int, input().split())

    if right % left == 0:
        print (left,right)
    else:
        print(left, right - (right%left))