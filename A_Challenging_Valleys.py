# def solve(arr):
#     if len(arr) == 1:
#         return "YES"
#     left = 0
#     right = 0
#     isValley = False
#     while right < len(arr) - 1:
#         if left - 1 >= 0 and arr[left-1] <= arr[left]:
#             left += 1
#             right = left
#         elif arr[left] == arr[right+1]:
#             right += 1
#         elif arr[right+1] > arr[left] or right + 1 == n:
#             # print(left,right)
#             if isValley:
#                 return "NO"
#             isValley = True
#             right = right+1
#             left = right
#         else:
#             right = right+1
#             left = right

    # if arr[right-1] > arr[left]:
    #     if isValley:
    #         return "NO"
    #     return "YES"
    
    # return "YES" if isValley else "NO"


def solve(arr):
    stack = []
    for i in range(len(arr)):
        if not stack:
            stack.append()
        



test = int(input())
for _ in range(test):
    n = int(input())    
    arr = list(map(int,input().split()))
    print(solve(arr))

