test = int(input())

for _ in range(test):
    n = int(input())
    array = list(map(int,input().split()))

    left = 0
    right = n-1
    sequence = []

    while left < right:
        sequence.append(array[left])
        sequence.append(array[right])
        left += 1
        right -= 1

    if left == right:
        sequence.append(array[left])

    print(*sequence)

