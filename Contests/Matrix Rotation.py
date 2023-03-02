
def transpose(arr):
    # trans = [[0,0], [0,0]]
    # for row in range(len(arr)):
    #     for col in range(len(arr[0])):
    #         trans[row][col] = arr[col][row]
    # print(trans)
    
    # return trans

    temp1 = arr[0][0]
    temp2 = arr[1][0]
    temp3 = arr[0][1]
    temp4 = arr[1][1]
    arr[0][0] = temp2
    arr[0][1] = temp1
    arr[1][0] = temp4
    arr[1][1] = temp3
def isBeautiful(arr):
    if arr[0][0] >= arr[0][1] or arr[0][0] >= arr[1][0]:
        return False
    if arr[0][1] >= arr[1][1] or arr[1][0] >= arr[1][1]:
        return False
    return True

test = int(input())

for _ in range(test):

    matrix = []

    matrix.append(list(map(int,input().split())))
    matrix.append(list(map(int,input().split())))

    beautiful = False

    for i in range(4):
        if isBeautiful(matrix):
            beautiful = True
            break
        else:
            transpose(matrix)
    if beautiful:
        print("YES")
    else:
        print("NO")
        

