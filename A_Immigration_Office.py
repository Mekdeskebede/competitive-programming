def solve(name, new):
 
    left = 0
    right = len(name) - 1

    while left <= right:
        mid = left + (right-left)//2

        if name[mid] < new:
            left = mid +1 
        else:
            right = mid - 1
    return left

n = int(input())
names = input().split()
q = int(input())
new = []
for _ in range(q):
    new.append(input())
for i in range(q):
    print(solve(names,new[i]))
