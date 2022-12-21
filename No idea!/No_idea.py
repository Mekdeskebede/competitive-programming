# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())

arr = list(map(int,input().split())) 
A = set(map(int,input().split()))
B = set(map(int,input().split()))

happy = 0
for i in arr:
    if i in A and i in B:
        continue
        
    elif i in A:
        happy += 1
    elif i in B:
        happy -= 1
print(happy)