# Enter your code here. Read input from STDIN. Print output to STDOUT
test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    
    l = 0
    r = len(arr) - 1
    top = float('inf')
    check = True
    while l < r:
        if top >= arr[r] and arr[r] >= arr[l]:
            top = arr[r]
            r -= 1
        elif top >= arr[l] and arr[l] > arr[r]:
            top = arr[l]
            l += 1
        else:
            check = False
            break
    print('Yes') if check  else print('No')