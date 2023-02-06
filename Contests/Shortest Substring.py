test = int(input())

for _ in range(test):
    s = input()

    min_ = float('inf')
    l = 0
    num = {}
    for r in range(len(s)):
        num[s[r]] = num.get(s[r],0) + 1

        while len(num) == 3 and l <= r:
            min_ = min(min_, r - l + 1)
            num[s[l]] -= 1
            if num[s[l]] == 0:
                num.pop(s[l])
            l += 1
            
    if min_ == float('inf'):
        print(0)
    else:
        print(min_)
        


