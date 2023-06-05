def solve(n):
    if int(n) % 25 == 0:
        return 0
    step = 0
    while n[-1] != 0 or n[-1] != 5:
        step += 1
        n = n[:-1]
    if int(n) % 25 == 0:
        return step
    

test = int(input())
for _ in range(test):
    n = input()