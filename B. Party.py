from collections import defaultdict

n = int(input())

adj_list = defaultdict(list)

for i in range(n):
    num = int(input())
    if num == -1:
        continue
    adj_list[i+1].append(num)



def dfs(node):
    count = 0
    
    for adj in adj_list[node]:
        count += dfs(adj)
            
    return count + 1

minimum = 1
for i in range(1,n+1):
    minimum = max(minimum,dfs(i))

if minimum >= 3:
    print(3)
else:
    print(minimum)


