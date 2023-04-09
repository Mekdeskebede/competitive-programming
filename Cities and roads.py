from collections import defaultdict

n = int(input())
adj_mat = []
edge_list = set()
for i in range(n):
    adj_mat.append(list(map(int,input().split())))

for row in range(n):
    for col in range(n):
        if adj_mat[row][col] == 1:
            if (col+1,row+1) not in edge_list:
                edge_list.add((row+1,col+1))

print(len(edge_list))