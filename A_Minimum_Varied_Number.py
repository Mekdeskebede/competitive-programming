def solve(n):
    if n < 10:
        return n
    ans = []
    first_num = 9
    while n:
        if first_num >= n:
            ans.append(str(n))
            break
        ans.append(str(first_num))
        n-= first_num
        first_num -= 1
    return "".join(ans[::-1])
        
test = int(input())
for _ in range(test):
    n = int(input())
    print(solve(n))


