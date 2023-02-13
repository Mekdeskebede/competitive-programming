n,m,k = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append(input())

ways = 0
for row in range(n):
    empty = 0
    for col in range(m):
        if matrix[row][col] == ".":
            empty += 1
            if empty >= k:
                ways += 1 
        else:
            empty = 0
for col in range(m):
    empty = 0
    for row in range(n):
        if matrix[row][col] == ".":
            empty += 1
            if empty >= k:
                ways += 1 
        else:
            empty = 0

print(ways)