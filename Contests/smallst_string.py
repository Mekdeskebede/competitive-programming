test = int(input())


for _ in range(test):
    n,m,k = map(int, input().split())

    s1 = input()
    s2 = input()
    s1 = sorted(s1)
    s2 = sorted(s2)
    step1 = k
    step2 = k

    c = ""
    p1 = 0
    p2 = 0

    while p1<n and p2<m:

        if s1[p1] < s2[p2]:
            if step1 == 0:
                c += s2[p2]
                step2 -= 1
                p2 += 1
                step1 = k
            else:
                c += s1[p1]
                p1 += 1
                step1 -= 1
                step2 = k
        else:
            if step2 == 0:
                c += s1[p1]
                step1 -= 1
                p1 += 1
                step2 = k
            else:
                c += s2[p2]
                p2 += 1
                step2 -= 1
                step1 = k

    print(c)


