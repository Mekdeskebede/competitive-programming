n = int(input())
cards = list(map(int,input().split()))
left = 0
right = n - 1
sereja = 0
dima = 0
while left < right:
    if cards[left] >= cards[right]:
        sereja += cards[left]
        left += 1
    elif cards[left] < cards[right]:
        sereja += cards[right]
        right -= 1
    if cards[left] >= cards[right]:
        dima += cards[left]
        left += 1
    elif cards[left] < cards[right]:
        dima += cards[right]
        right -= 1
if left == right:
    sereja += cards[left]
print( str(sereja) + " " + str(dima))
