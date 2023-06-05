n = int(input())
arr = list(map(int,input().split()))
prev = 0
count = 0
for i in range(n):
    if arr[i] == 0:
        prev = 0
    elif arr[i] == 3:
        count += 1
        if prev == 2:
            prev = 1
        elif prev == 1:
            prev = 2
        else:
            if i+1 < n:
                if arr[i+1] == 1:
                    prev = 2
                elif arr[i+1] == 2:
                    prev = 1
    elif arr[i] == 2:
        if prev == 2:
            prev = 0
        elif prev == 1:
            count += 1
            prev = 2
        elif prev == 0:
            count += 1
            prev = 2
    else:
        if prev == 1:
            prev = 0
        elif prev == 2:
            count += 1
            prev = 1
        elif prev == 0:
            count += 1
            prev = 1
print(n-count)
                    

