test = int(input())

for _ in range(test):
    
    value = {"S":1, "M":2, "L":3}
    
    a, b = input().split()
    
    if value[a[-1]] > value[b[-1]]:
        print(">")
    elif value[a[-1]] < value[b[-1]]:
        print("<")
    else:
        if len(a) == len(b):
            print("=")
        elif a[-1] == "S":
            if len(a)> len(b):
                print("<")
            else:
                print(">")
        else:
            if len(a)> len(b):
                print(">")
            else:
                print("<")