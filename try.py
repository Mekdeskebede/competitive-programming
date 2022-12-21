
def merge( nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    arr = []
    
    p1 = 0
    p2 = 0
    
    while p1 < m and p2 < n:
        if nums1[p1] <= nums2[p2]:
            arr.append(nums1[p1])
            p1 += 1
        else:
            arr.append(nums2[p2])
            p2 += 1
    arr += nums1[p1:m] + nums2[p2:n]
    nums1[:] = arr[:]
    return(nums1)
print(merge([1,2,3,0,0,0],3,[2,5,6],3))