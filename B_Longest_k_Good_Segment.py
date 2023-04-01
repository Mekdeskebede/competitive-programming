from collections import defaultdict

def soln(arr,k,n):
    seen = defaultdict(int)
    left = 0
    max_len = 1
    lr = (1,1)
    for right in range(n):
        seen[arr[right]] += 1

        while len(seen) > k:
            seen[arr[left]] -= 1
            if seen[arr[left]] ==0:
                del seen[arr[left]]
            left += 1
        if right - left + 1 > max_len:
            max_len = right-left+1
            lr = (left+1,right+1)
    return lr

n, k = map(int,input().split())
arr = list(map(int,input().split()))
print(*soln(arr,k,n))
