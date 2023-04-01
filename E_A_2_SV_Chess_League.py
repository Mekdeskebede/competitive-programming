# n , k = map(int,input().split())
# arr = list(map(int,input().split()))

def mergeSort(arr,left_arr,right_arr,k):

    # new = []
    # left = 0
    # right = 0
    # while left < len(left_arr) and right < len(right_arr):
    #     if left_arr[left] < right_arr[right]:
    #         new.append(left_arr[left])
    #         left += 1
    #     else:
    #         new.append(right_arr[right])
    #         right += 1
    # new.extend(right_arr[right:])
    # new.extend(left_arr[left:])
    # return new

    left = 0
    right = 0
    while left < len(left_arr) and right < len(right_arr):

        if abs(arr[left_arr[left]]-arr[right_arr[right]]) > k:
            print("here")
            return left_arr[left:] + right_arr[right:]
        elif left_arr[left] > right_arr[right]:
            right += 1
        else:
            left += 1
    return left_arr[left:] + right_arr[right:]

def merge(left, right,arr):
    if left == right:
        return [left]
    mid = left + (right-left)//2
    left_arr = merge(left,mid,arr)
    right_arr = merge(mid+1,right,arr)
    
    return mergeSort(arr,left_arr,right_arr,k)

# print((merge(0,2*n-1,arr)))


n, k= list(map(int, input().split()))
rating= list(map(int, input().split()))
     
def merge(arr1, arr2):
    p1,p2 = 0,0
    res= []
    while p1 < len(arr1) and p2 < len(arr2):
        # print(rating[arr1[p1]], rating[arr2[p2]])
        if abs(rating[arr1[p1]] - rating[arr2[p2]]) > k:
            if rating[arr1[p1]] < rating[arr2[p2]]:
                p1+=1
            else:
                p2 += 1
            continue
        if rating[arr1[p1]] < rating[arr2[p2]]:
            res.append(arr1[p1])
            p1 += 1
        else:
            res.append(arr2[p2])
            p2 +=1
    res.extend(arr2[p2:])
    res.extend(arr1[p1:])
    return res
        
def A2SV_verses(rating, k, start, end):
    if start == end:
        return [start]
    
    mid= (start + end) // 2
    arr1= A2SV_verses(rating, k, start, mid)
    arr2= A2SV_verses(rating, k, mid + 1, end)
    
    return merge(arr1, arr2)
print(*sorted(map(lambda x:x+1,A2SV_verses(rating, k, 0, len(rating)-1))))

