
test = int(input())

for i in range(test):

    n = int(input())
    ball = list(map(int, input().split()))
    
    ball_idx = []
    for idx, val in enumerate(ball):
        ball_idx.append((val, idx))
    ball_idx.sort()

    print(ball_idx[-1][1] + 1)