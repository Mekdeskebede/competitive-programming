from collections import defaultdict, deque
test = int(input())
for _ in range(test):

    input()
    n, k = map(int, input().split())
    incoming = defaultdict(int)
    adj_list = defaultdict(list)
    nodes = set()

    for i in range(n-1):
        start, end = map(int, input().split())
        adj_list[start].append(end)
        adj_list[end].append(start)
        incoming[end] += 1
        incoming[start] += 1

    queue  = deque()
    for key in incoming:
        if incoming[key] == 1:
            queue.append(key)

    while queue and k-1:
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            for neighbor in adj_list[node]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 1:
                    queue.append(neighbor)
        k -= 1

    count = 0
    for key in incoming:
        if incoming[key] > 1:
            count += 1

    print(count)
    
            
    

