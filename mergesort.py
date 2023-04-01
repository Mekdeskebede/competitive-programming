def merge(left_h,right_h):
    new = []
    left = 0
    right = 0
    while left < len(left_h) and right < len(right_h):
        if left_h[left] < right_h[right]:
            new.append(left_h[left])
            left += 1
        else:
            new.append(right_h[right])
            right += 1
    new.extend(right_h[right:])
    new.extend(left_h[left:])
    return new

def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)

    return merge(left_half, right_half)

def test():
    assert mergeSort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10]
    assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3]
    assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3]
    print("Great Job !!!")

test()

