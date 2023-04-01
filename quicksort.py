def merge(w,r,arr):
    while r < len(arr):
        if arr[0] < arr[r]:
            arr[w], arr[r] = arr[r], arr[w]
    arr[0], arr[w-1] = arr[w-1], arr[0]

def quickSort(start,end, arr):
    if end - start <= 0:
        return
    w = start + 1
    for r in range(start+1, end+1):
        if arr[start] >= arr[r]:
            arr[w] , arr[r] = arr[r] , arr[w]
            w += 1
    arr[start] , arr[w-1] = arr[w-1], arr[start]
    quickSort(start,w-2,arr)
    quickSort(end,w,arr)
arr = [3]
quickSort(0, 0,arr)
print(arr)
# def test():
#     assert quickSort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10]
#     assert quickSort(0, 0, [1]) == [1]
#     assert quickSort(0, 2, [3, 2, 1]) == [1, 2, 3]
#     print("Great Job !!!")

# test()

