def trial_division_simple(n):
    almost_prime = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            almost_prime.add(d)
            n //= d
        d += 1
    if n > 1:
        almost_prime.add(n)

    if len(almost_prime) == 2:
        return True
    return False

num = int(input())
res = 0
for i in range(1,num+1):
    if trial_division_simple(i):
        res += 1
print(res)

