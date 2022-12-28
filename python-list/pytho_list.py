if __name__ == '__main__':
    
    lst = []
    N = int(input())
    
    for _ in range(N): 
        cmd = input().split()
        first =  cmd[0]
        if first == 'insert':
            lst.insert(int(cmd[1]), int(cmd[2]))
        elif first == 'print':
            print(lst)
        elif first == 'remove':
            lst.remove(int(cmd[1]))
        elif first == 'append':
            lst.append(int(cmd[1]))
        elif first == 'sort':
            lst.sort()
        elif first == 'pop':
            lst.pop()
        elif first == 'reverse':
            lst.reverse()
            
    