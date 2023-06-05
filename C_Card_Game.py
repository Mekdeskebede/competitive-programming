def solve(n,card1, card2):
    card1.sort()
    card2.sort()
    p1, p2 = n-1, n-1
    count = 0
    while p1 > -1 and p2 > -1:
        if card1[p1] > card2[p2]:
            p1 -= 1
        else:
            count += 1
            p1 -= 1
            p2 -= 1
    if count > n//2:
        return True
    return False

n = int(input())
mati = list(map(int, input().split()))
ibsa = list(map(int, input().split()))

if solve(n,mati,ibsa):
    print("YES")
else:
    print("NO")