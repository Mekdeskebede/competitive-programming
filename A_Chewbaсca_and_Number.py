num = input()

def soln(num,ans):      
    for digit in num:
        if ans == "" and (digit == "9" or digit == "0"):
            ans += "9"
            continue
        else:
            ans += str(min(int(digit),9-int(digit)))
    return int(ans)
print(str(soln(num,"")))
