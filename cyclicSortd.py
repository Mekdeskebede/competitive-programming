def cycleSort(arr):
    
    for i in range(len(arr)):
        while i + 1 != arr[i]:
            temp = arr[i]-1
            arr[i], arr[temp] = arr[temp], arr[i]
    return arr
    # return [i+1 for i in range(len(arr)) ]

print(cycleSort([3,5,1,4,2]))

