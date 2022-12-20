# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
grp = list(map(int,input().split()))
count = {}
for i in range(len(grp)):
    count[grp[i]] = 1 + count.get(grp[i],0)

for g in grp:
    if count[g] != k:
        print(g)