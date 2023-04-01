line = int(input())
cmd = []
for _ in range(line):
    c = input()
    if c == "add":
        cmd.append([1])
    elif c == "end":
        cmd.append([c])
    else:
        cmd.append(c.split())
# print(cmd)
stack = []
for c in cmd:
    if c == ["end"]:
        temp = []
        while stack and len(stack[-1]) != 2:
            temp.append(stack.pop())
        f , v = stack.pop()
        temp = [[i[0] * int(v)] for i in temp]
        stack += temp
print(stack)
    