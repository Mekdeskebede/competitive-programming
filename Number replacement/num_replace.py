test = int(input())

for _ in range(test):
    
    n = int(input())
    nums = input().split()
    letters = input()
    
    pairs = {}
    count = 0
    for i in range(n):
        if nums[i] in pairs and pairs[nums[i]] != letters[i]:
            break
        pairs[nums[i]] = letters[i]
        count += 1
        
    if count < n:
        print("NO")
    else:
        print("YES")