test = int(input())

for _ in range(test):
    n, k = map(int,input().split())
    binary = bin(k)
    binary = binary[2:]
    ans = 0
    j = len(binary) - 1
    for i in range(j,-1,-1):
        if binary[i] == "1":
            ans += n ** (j-i)
    print(ans%(10**9 +7))
    
