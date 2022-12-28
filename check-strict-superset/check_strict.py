# Enter your code here. Read input from STDIN. Print output to STDOUT

set_a = set(input().split())
n = int(input())
res = []
for _ in range(n):
    
    other = set(input().split())
    count = 0
    m = len(other)
    
    for num in other:
        if num not in set_a:
            break
        else:
            count += 1
    if count == m and m < len(set_a):
        res.append(True)
    else:
        res.append(False)

if all(res):
    print("True")
else:
    print("False")