from collections import Counter

test = int(input())

for _ in range(test):
    
    n , c = map(int,input().split())
    orbits = Counter(input().split())
    
    ans = 0
    for planets in orbits.keys():
        
        if orbits[planets] > c:
            ans += c
        else:
            ans += orbits[planets]
    print(ans)
        