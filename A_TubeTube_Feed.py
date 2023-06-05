test = int(input())
for _ in range(test):
    n,t = map(int, input().split())
    arr = list(map(int, input().split()))
    ent = list(map(int, input().split()))
    possibles = []
    for i in range(n):
        if arr[i] + i <= t:
            possibles.append([ent[i],i])
    if not possibles:
        print(-1)
    else:
        maximum = max(possibles)
        print(maximum[1]+1)