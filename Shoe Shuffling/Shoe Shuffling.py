test = int(input())
for i in range(test):
    stu = int(input())
    shoe = list(map(int, input().split()))

    swapped = False
    left = 0
    right = 1
    res = [str(i) for i in range(1,stu+1)]
    while right < stu:
        if shoe[left] >= shoe[right]:
            swapped = True
            res[left] , res[right] = res[right], res[left]
            left += 1
            right += 1
        elif swapped and shoe[left] < shoe[right]:
            swapped = False
            right += 1
            left += 1
        else:
            print(-1)
            break
    if right >= stu:
        print(" ".join(res))
