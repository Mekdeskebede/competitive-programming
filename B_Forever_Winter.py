from collections import defaultdict, deque


test = int(input()) 
for _ in range(test):
    n, m = map(int, input().split())
    adj_list = defaultdict(list)
    incoming = defaultdict(int)
    for i in range(m):
        start, end = map(int, input().split())
        adj_list[start].append(start)
        adj_list[end].append(end)
        incoming[start] += 1
        incoming[end] += 1
    
    queue = deque()
    for key in incoming:
        if incoming[key] == 1:
            queue.append(key)
    x_and_y = len(queue)
    x = n - 1 - x_and_y
    print(x, x_and_y//x)
        