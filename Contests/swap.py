n = int(input())
array = list(map(int,input().split()))

swap = 0
swaps = []

for i in range(n):
    idx = i
    for j in range(i+1,n):
        if array[j] < array[idx]:
            idx = j
    array[idx] , array[i]= array[i], array[idx]
    if idx != i:
        swap += 1
        swaps.append((i,idx))
print(swap)
for first, second in swaps:
    print(first,second)

        

