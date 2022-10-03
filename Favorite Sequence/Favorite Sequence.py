for _ in range(int(input())):
    n = int(input())
    arr = list(input().split())

    left = 0
    right = n - 1
    ans = []
    while left <= right:
        if left == right:
            ans.append(arr[left])
            break
        else:
            ans.append(arr[left])
            ans.append(arr[right])
            left += 1
            right -= 1
    print(" ".join(ans))

