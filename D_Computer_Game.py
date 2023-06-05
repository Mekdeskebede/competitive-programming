test = int(input())    

for _ in range(test):
    n = int(input())
    adj_matix = [[],[]]
    for i in input():
        adj_matix[0].append(int(i))
    for i in input():
        adj_matix[1].append(int(i))
    visited  = set()
    isPossible = False
    
    def soln(n):
        # print(adj_matix,n)  
        directions = [[0,1], [1,0], [1,1], [-1,-1], [1,-1],[-1,1],[-1,0], [0,-1]]
        def inBound(row,col):
            return 0 <= row < 2 and 0 <= col < n
        isPossible = False
        visited = set()
        def dfs(row,col):
            nonlocal isPossible
            visited.add((row,col))

            if row == 1 and col == n-1:
                isPossible = True
                return
            for r,c in directions:
                if inBound(r+row,c+col) and adj_matix[row+r][col+c] == 0 and (row+r,col+c) not in visited:
                    dfs(row+r,col+c) 
        dfs(0,0) 
        if isPossible:
            print("YES")
        else:
            print("NO")
    soln(n)

    
    
