from collections import Counter


string = input()
kitchen = list(map(int,input().split()))
price = list(map(int,input().split()))
rubles = int(input())
s_count = Counter(string) 
k_count = {"B":kitchen[0], "S":kitchen[1], "C":kitchen[2]}
# print(k_count)
res = 0
# print(rubles)
while rubles > 0:
    print("here")
    print(k_count)
    if s_count["B"] >= k_count["B"]:
        k_count["B"] -= s_count["B"]
        print("here")
    elif s_count["B"] < k_count["B"]:
        left = s_count["B"] - k_count["B"]
        if rubles - (left * price[0]) >= 0:
            rubles -= left * price[0] 
        else:
            break
    if s_count["S"] >= k_count["S"]:
        k_count["S"] -= s_count["S"]
    elif s_count["S"] < k_count["S"]:
        left = s_count["S"] - k_count["S"]
        if rubles - left * price[1] >= 0:
            rubles -= left * price[1] 
        else:
            break
    if s_count["C"] >= k_count["C"]:
        k_count["C"] -= s_count["C"]
    elif s_count["C"] < k_count["C"]:
        left = s_count["C"] - k_count["C"]
        if rubles - left * price[2] >= 0:
            rubles -= left * price[2] 
        else:
            break
    res += 1

print(res)
    


