import heapq

test = int(input())

for _ in range(test):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    heapq.heapify(a)

    p = 0
    while p < m:
        heapq.heappop(a)
        heapq.heappush(a,b[p])
        p += 1
        
    print(sum(a))