n = int(input())
cards = m=list(map(int,input().split())) 
wube = 0
henok = 0

left = 0
right = n-1
even = True
while left <= right:
    if even:
        if cards[left] > cards[right]:
            wube += cards[left]
            left += 1
        else:
            wube += cards[right]
            right -= 1
        even = False
    else:
        if cards[left] > cards[right]:
            henok += cards[left]
            left += 1
        else:
            henok += cards[right]
            right -= 1
        even = True
print(wube,henok)
