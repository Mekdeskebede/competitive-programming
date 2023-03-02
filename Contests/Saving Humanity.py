def solve(n,m,arr):
    if sum(arr) == 0:
        return arr
    for i in range(m):
    
        before = arr[:]

        for j in range(n):
            
            if before[j] == 1:
                continue
            elif (j - 1 >= 0 and before[j-1] == 1) and (j + 1 < n and before[j+1] == 1):
                continue
            elif j - 1 >= 0 and before[j-1] == 1 :
                arr[j] = 1
            elif j + 1 < n and before[j+1] == 1:
                arr[j] = 1
        if before == arr:
            return arr
    return arr

test = int(input())

for _ in range(test):
    n, m = map(int,input().split())

    arr = list(input())

    arr = list(map(int, arr))

    res_arr = solve(n,m,arr)
    res_arr = list(map(str,res_arr))
    print("".join(res_arr))



