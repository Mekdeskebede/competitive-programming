n, k= list(map(int, input().split()))
rating= list(map(int, input().split()))

def merge(arr1, arr2):
    p1,p2 = 0,0
    res= []
    while p1 < len(arr1) and p2 < len(arr2):
        if abs(rating[arr1[p1]] - rating[arr2[p2]]) > k:
            if rating[arr1[p1]] >= rating[arr2[p2]]:
                p2+=1
            else:
                p1 += 1
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
        
def mergeSort(rating, k, start, end):
    if start == end:
        return [start]
    
    mid= (start + end) // 2
    arr1= mergeSort(rating, k, start, mid)
    arr2= mergeSort(rating, k, mid + 1, end)
    
    return merge(arr1, arr2)
ans = mergeSort(rating, k, 0, len(rating)-1)
ans = sorted(map(lambda x:x+1,ans))
print(*ans)

