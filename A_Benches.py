n = int(input())
m = int(input())
benches = []
for _ in range(n):
    benches.append(int(input()))
maximum = max(benches) + m
large = max(benches)
i = 0
for i in range(n):
    if not m:
        break
    temp = large - benches[i]
    benches[i] += min(temp,m)
    m -= min(temp,m)
if m:
    if not m%n:
        minimum = max(benches) + m // n 
    else:
        minimum = max(benches) + m // n + 1
else:
    minimum = max(benches)
print(minimum,maximum)


