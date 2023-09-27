from collections import Counter


def longestString(a,b):
    dictionary = {}
    for c in b:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1
    n = len(a)
    for i in range(n):
        if a[i] in dictionary and dictionary[a[i]] > 0:
            dictionary[a[i]] -= 1
        else:
            return i
    return n


testcase = int(input())
for _ in range(testcase):
    str1,str2 = input().split(" ")
    print(longestString(str1,str2))
