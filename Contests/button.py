test = int(input())

for _ in range(test):
    s = str(input())

    n = len(s)
    if n < 2:
        print(s)
    else:
        left = 0
        right = 1
        correct = ""
        while right < n:
            if s[right] != s[left]:
                correct+=s[left]
                left += 1
                right += 1
            else:
                left += 2
                right += 2
        if left==n-1:
            correct +=s[left]
        if correct:
            correct = sorted(correct)
            correct = "".join(correct)
        print(correct)
            




