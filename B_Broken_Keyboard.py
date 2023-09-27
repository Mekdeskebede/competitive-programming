for i in range(int(input())):
    string = input()
    left = 0
    right = 1
    res = []
    while right < len(string):
        if string[right] == string[left]:
            left += 2
            right += 2
        else:
            if string[left] not in res:
                res.append(string[left])
            left += 1
            right += 1
    if left == len(string) -1:
        if string[left] not in res:
                res.append(string[left])
    res.sort()
    print(''.join(res))