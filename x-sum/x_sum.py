from collections import defaultdict

test = int(input())

for _ in range(test):
    
    n, m = map(int,input().split())
    matrix = []
    
    for i in range(n):
        row = list(map(int,input().split()))
        matrix.append(row)
    
    left_diagonal = defaultdict(int)
    right_diagonal = defaultdict(int)
    
    for row in range(n):
        for col in range(m):
            left_diagonal[row-col] += matrix[row][col] 
            right_diagonal[col+row] += matrix[row][col]

    maximum = 0
    for row in range(n):
        for col in range(m):
            total = (left_diagonal[row-col] + right_diagonal[row+col]) - matrix[row][col]
            maximum = max(maximum, total)

    print (maximum)
    

        
        
