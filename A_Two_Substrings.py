# s = input()
# hashtable = {}
# for i in range(len(s)-1):
#     if s[i:i+2] == "AB" or s[i:i+2] == "BA":
#         hashtable[i] = s[i:i+2]
# index = list(hashtable.keys())
# flag = False
# for i in range(len(index)):
#     if flag:
#         break
#     for j in range(i+1,len(index)):
#         if hashtable[index[i]] != hashtable[index[j]] and abs(index[i]-index[j]) >= 2:
#             flag = True
#             print("YES")
#             break
# if not flag:
#     print("NO")

def solve(s):
    ab = None
    ba = None
    for i in range(len(s)-1):
        if s[i:i+2] == "AB":
            if ba!= None and abs(i-ba) >= 2:
                return True
            if ab!=None:
                ab = min(i,ab)
            else:
                ab = i
        if s[i:i+2] == "BA":
            if ab != None and abs(i-ab) >= 2:
                return True
            if ba!=None:
                ba = min(i,ba)
            else:
                ba = i
    return False

s = input()
if solve(s):
    print("YES")
else:
    print("NO")

