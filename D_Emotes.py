n, m , k = map(int, input().split())
emotes = list(map(int, input().split()))

emotes.sort()
count = k
x = m//k - 1
ans = emotes[-2]*(x) + (m-x)* emotes[-1]

print(ans)