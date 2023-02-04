brackets = str(input())

left = 0
right = len(brackets)-1
removed_l = []
removed_r = []
operation = 0
while left < right:
    if brackets[left] == "(" and brackets[right] == ")":
        removed_l.append(left+1)
        removed_r.append(right+1)
        left += 1
        right -= 1
        operation = 1
    else:
        right -= 1
removed =removed_l+removed_r
print(operation)
if removed:
    print(len(removed))
    print(*removed)
