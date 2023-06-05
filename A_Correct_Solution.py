def soln(alice,bob):
    num = sorted(list(alice))
    if num [0] != "0"  or len(num) == 1:
        return "".join(num) == bob
    zero = 0
    while zero < len(num) and num[zero] == "0":
        zero += 1
    num[0],num[zero] = num[zero], num[0]
    return "".join(num) == bob

if soln(input(), input()):
    print('OK')
else:
    print("WRONG_ANSWER")
    