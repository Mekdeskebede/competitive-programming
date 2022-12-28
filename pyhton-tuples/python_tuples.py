# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
tpl = tuple(map(int,input().split()))
res = hash(tpl)
print(res)
