from collections import Counter
def solve(arr):
    count = Counter(arr)
    sticks = list(count.keys())
    sticks.sort()
    left = 0
    right = len(sticks) - 1
    prev = None
    while left <= right:
        if count[sticks[left]] >=2 and count[sticks[right]] >= 2:
            if not prev:
                prev = sticks[left] * sticks[right]
            elif prev != sticks[left] * sticks[right]:
                return False
            count[sticks[left]] -= 2
            count[sticks[right]] -= 2
            if count[sticks[left]] == 0:
                left += 1
            if count[sticks[right]] == 0:
                right -= 1   
        else:
            return False
    return True

q = int(input())

for _ in range(q):
    n = int(input())
    arr = list(map(int,input().split()))
    
    if solve(arr):
        print("YES")
    else:
        print("NO")

