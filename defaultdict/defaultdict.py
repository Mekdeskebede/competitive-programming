# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m = map(int,input().split())
grpA = defaultdict(list)
grpB = []

for a in range(n):
    grpA[input()].append(str(a+1))
    
for b in range(m):
    key = input()
    if key in grpA:
        print(" ".join(grpA[key]))
    else:
        print(-1)
    
