n,m = map(int, input().split())
query = []

for _ in range(m):
    query.append(tuple(map(int, input().split())))
def soln(n,query):
    days = [0] * n
    for start,end in query:
        days[start] += 1
        if end + 1 < n:
            days[end+1] -= 1

    for i in range(1,n):
        days[i] += days[i-1]
    
    for num in days:
        if num <=0:
            return False
    return True

if soln(n,query):
    print("NO")
else:
    print("YES")
