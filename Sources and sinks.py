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
            # adj_list[col+1].append(row + 1)
sink = []
end = []
for key in range(1,n+1):
    if key not in adj_list:
        sink.append(key)
    end.extend(adj_list[key])

source = []
end = set(end)
for v in range(1,n+1):
    if v not in end:
        source.append(v)

print(len(source), *source)
print(len(sink), *sink)

