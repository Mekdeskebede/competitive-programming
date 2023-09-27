n = int(input())
first = list(map(int,input().split()))
second = list(map(int,input().split()))
level = [i for i in range(1,n+1)]
ans = set(first[1:]+second[1:])

if ans == set(level):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

