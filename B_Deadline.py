import math

def solve(n,d):
    if n >= d:
        return "YES"
    temp = 0
    while temp < n and temp < d:
        if temp + math.ceil(d/(temp+1)) <= n:
            return "YES"
        temp += 1
    return "NO"

test = int(input())
for _ in range(test):
    n, d= map(int,input().split())
    print(solve(n,d))