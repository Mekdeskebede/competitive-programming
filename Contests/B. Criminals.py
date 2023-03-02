def soln(n,arr):
    
    for idx in range(n-1):
        if arr[idx] != 0:
            break

    zeros = arr[idx+1:n-1].count(0)
    non_zeros = sum(arr[idx:n-1])

    return zeros + non_zeros

test = int(input())

for _ in range(test):

    n = int(input())
    arr = list(map(int,input().split()))

    operation = soln(n,arr)

    print(operation)


    

