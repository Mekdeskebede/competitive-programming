from collections import defaultdict

n = int(input())
adj_mat = []
adj_list = defaultdict(list)
for i in range(n):
    adj_mat.append(list(map(int,input().split())))

for row in range(n):
    for col in range(n):
        if adj_mat[row][col] == 1:
            adj_list[row+1].append(col+1)