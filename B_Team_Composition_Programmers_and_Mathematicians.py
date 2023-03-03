def solve(a,b):
    
    team = min((a+b)//4,a,b)
    return team

test = int(input())

for _ in range(test):
    a, b = map(int,input().split())
    print(solve(a,b))
