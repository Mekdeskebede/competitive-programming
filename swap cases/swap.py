def swap_case(s):
    mod = []
    for i in s:
        if i.isupper():
            mod.append(i.lower())
        else:
            mod.append(i.upper())
    return ''.join(mod)

# if __name__ == '__main__':