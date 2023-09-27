def solve(arr):
    index = {}
    pre_sum1 = []
    pre = 0
    for i in range(len(arr)):
        pre += arr[i]
        pre_sum1.append(pre)
        index[pre] = i
    max_ = 0
    curr = 0
    for i in range(len(arr)-1, -1,-1):
        curr += arr[i]
        if curr in index and i > index[curr]:
            max_ = max(max_, index[curr] + len(arr)-i+1)
    return max_

n = int(input())
for _ in range(n):
    m = int(input())    
    arr = list(map(int,input().split()))
    print(solve(arr))


# def solve(arr):
#       max_= 0     
#       if len(arr) == 1:
#             return 0
#       left = 0
#       right = len(arr)-1
#       alice = arr[left] 
#       bob = arr[right]
#       while left < right:
#             if alice != 0 and alice == bob:
#                   max_= max(max_, (len(arr) - right) + left + 1)
            
#             if alice < bob:
#                   left += 1
#                   alice += arr[left]
#             else:
#                   right -= 1
#                   bob += arr[right]
#       return max_

# n = int(input())
# for _ in range(n):
#     m = int(input())    
#     arr = list(map(int,input().split()))
#     print(solve(arr))