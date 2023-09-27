test = int(input())
for _ in range(test):
    n = int(input())
    start = list(map(int, input().split()))
    duration = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if i == 0:
            ans.append(duration[i]-start[i])
        elif duration[i-1] >= start[i]:
            ans.append(duration[i]-duration[i-1])
        else:
            ans.append(duration[i]-start[i])
            
    print(*ans)