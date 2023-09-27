from collections import Counter


def solve(a,b,c):
    count = {"a":a, "b":b, "c":c}
    ans = 0
    unique = set()
    if count["a"]:
        count["a"] -= 1
        unique.add("a")
        ans += 1
    if count["b"]:
        count["b"] -= 1
        unique.add("b")
        ans += 1
    if count["c"]:
        count["c"] -= 1
        unique.add("c")
        ans += 1
    if count["a"] and count["b"]:
        unique.add("ab")
        count["a"] -= 1
        count["b"] -= 1
        ans += 1
    if count["a"] and count["c"]:
        unique.add("ac")
        count["a"] -= 1
        count["c"] -= 1 
        ans += 1
    if count["b"] and count["c"]:
        unique.add("bc")
        count["c"] -= 1
        count["b"] -= 1 
        ans += 1
    if count["a"] and count["b"] and count["c"]:
        ans += 1
    return ans

test = int(input())
for _ in range(test):
    a,b,c = map(int, input().split())
    a,b,c = sorted([a,b,c], reverse=True)
    print(solve(a,b,c))