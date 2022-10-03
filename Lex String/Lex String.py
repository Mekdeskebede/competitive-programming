test = int(input())

for i in range(test):
    n, m, k = map(int,input().split())
    a = list(input())
    b = list(input())

    a.sort()
    b.sort()
    c = []

    a_ptr = 0
    b_ptr = 0
    a_limit = 0
    b_limit = 0

    while a_ptr < len(a) and b_ptr < len(b):

        if a[a_ptr] < b[b_ptr] and a_limit < k:
            c.append(a[a_ptr])
            a_ptr += 1
            a_limit += 1
            b_limit = 0
        elif a[a_ptr] > b[b_ptr] and b_limit < k:
            c.append(b[b_ptr])
            b_ptr += 1
            b_limit += 1
            a_limit = 0
        elif a_limit < k:
            c.append(a[a_ptr])
            a_ptr += 1
            a_limit += 1
            b_limit = 0
        elif b_limit < k:
            c.append(b[b_ptr])
            b_ptr += 1
            b_limit += 1
            a_limit = 0
        else:
            break
    print("".join(c)) 

    