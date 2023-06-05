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
    return count

n = int(input())
mati = list(map(int, input().split()))
ibsa = list(map(int, input().split()))

win = solve(n,mati,ibsa)
lose = n - win
if lose%2 == 0:
    print(lose//2)
else:
    print(lose//2+1)