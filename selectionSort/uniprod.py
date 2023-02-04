n = int(input())

array = list(map(int,input().split()))

negatives = []
cost = 0
for i in range(n):
    if array[i] >= 0 :
        cost += abs(array[i]-1)
    else:
        negatives.append(array[i])

m = len(negatives)
if len(negatives) == 1:
    cost += abs(array[-1]-1)

if len(negatives) > 1:
    if m%2 == 0:
        for j in range(m):
            cost += abs(array[j]+1)
    else:
        for j in range(m-1):
            cost += abs(array[j]+1)
        cost += abs(array[-1]-1)
print(cost)
