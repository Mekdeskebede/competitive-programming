def solve(s):
    count = 0
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            j += 1
        if j - i < 2:
            return "NO"
        i = j
    return "YES"

test = int(input())
for _ in range(test):
    print(solve(input()))