def solution(s):
    if len(s) == 0:
        return 1

    c = []

    for char in s:
        if c and c[-1] == char:
            c.pop()
        else:
            c.append(char)

    if len(c) == 0:
        return 1
    else:
        return 0
