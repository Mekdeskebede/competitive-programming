# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input())
li = []
for i in range(n):
    li.append(input())
count = {}
for string in li:
    # print(string)
    # count[string] = 1 + count.get(count[string],0)
    if string in count:
        count[string] += 1
    else:
        count[string] = 1
ans = []

for s , v in count.items():
    ans.append(str(v))
print(len(ans))
print(" ".join(ans))