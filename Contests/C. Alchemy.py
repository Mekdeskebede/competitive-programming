def soln(n,arr):
    if n == 1:
        return (1,0)
    left = 0
    right = n - 1
    ed = 0
    al = 0
    ed_count = 0
    al_count = 0

    while left <= right:
        if ed > al :
            al += arr[right]
            al_count += 1
            right -= 1
        elif al > ed:
            ed += arr[left]
            ed_count += 1
            left += 1
        else:
            if left == right:
                ed += arr[left]
                ed_count += 1
                left += 1
            else:
                ed += arr[left]
                ed_count += 1
                left += 1

    return (left, n - right-1)



n = int(input())
arr = list(map(int,input().split()))

print(*soln(n,arr))
