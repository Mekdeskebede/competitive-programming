# n,k = map(int,input().split())
# arr = list(map(int,input().split()))
# minimum = [sum(arr[:k]),0]
# currSum = sum(arr[:k])
# left = 0
# for right in range(k,n):
#     currSum -= arr[left]
#     left += 1
#     currSum += arr[right]
#     if currSum <= minimum[0]:
#         minimum = [currSum,left]
# print(minimum[1]+1)

n, m = map(int, input().split())
arr= list(map(int, input().split()))
idx = 0
p1 = 0
p2 = m
sum = sum(arr[:m])
minmum = sum
while p2 < n:
    sum -= arr[p1]
    sum += arr[p2]
    p1 += 1
    if sum < minmum:
        minmum = sum
        idx = p1
    p2 += 1
print(idx + 1)