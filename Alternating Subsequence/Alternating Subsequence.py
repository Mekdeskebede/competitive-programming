test = int(input())

for _ in range(test):
    n = int(input())
    array = list(map(int,input().split()))

    i = 0
    max_sum = 0
    while i < n:
        curr = array[i]
        j = i + 1
        if array[i] > 0:
            while j < n and array[j] > 0:
                curr = max(curr,array[j])
                j += 1
        else:
            while j < n and array[j] < 0:
                curr = max(curr,array[j])
                j += 1
        max_sum += curr
        i = j
    print(max_sum)
    




