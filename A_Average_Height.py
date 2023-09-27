test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    odd = []
    even = []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    print(*(odd+even))