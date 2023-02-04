def isPossible(arr):
    arr.sort()
    n = len(arr)
    left = 0
    right = 1

    while right < n:
        if (arr[right] - arr[left]) > 1:
            return False
        left += 1
        right += 1
    return True

test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    if isPossible(arr):
        print("YES")    
    else:
        print("NO")

    
