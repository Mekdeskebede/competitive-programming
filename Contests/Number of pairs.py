n = int(input())
boys = list(map(int, input().split()))

m = int(input())
girls = list(map(int, input().split()))

boys.sort()
girls.sort()

b = n - 1
g = m - 1
pairs = 0

while b >= 0 and g >= 0:
    if abs(boys[b] - girls[g]) < 2:
        pairs += 1
        g -= 1
        b -= 1
    else:
        if boys[b]> girls[g]:
            b -= 1
        else:
            g -= 1
print(pairs)
