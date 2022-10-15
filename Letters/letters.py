n,m = map(int,input().split())
dorm = list(map(int,input().split()))
letters = list(map(int,input().split()))
ptr = 0
dif = 0
for curr in letters:
	while(curr>dif+dorm[ptr]):
		dif+=dorm[ptr]
		ptr +=1
	print(ptr + 1, curr - dif)