def solution(n,k,q,recipes,questions):
    arr = [0] * 2000001

    for start, end in recipes:
        arr[start] += 1
        arr[end+1] -= 1
    pre_sum = 0
    for idx in range(len(arr)):
        pre_sum += arr[idx]
        arr[idx] = pre_sum

    for idx in range(len(arr)):
        if arr[idx] >= k:
            pre_sum += 1
        arr[idx] = pre_sum
    
    for start, end in questions:
        print(arr[end]-arr[start-1])
    

n, k ,q = map(int,input().split())
recipes = []
for i in range(n):
    recipes.append(list(map(int,input().split())))
questions = []

for i in range(q):
    questions.append(list(map(int,input().split())))

solution(n,k,q,recipes,questions)





