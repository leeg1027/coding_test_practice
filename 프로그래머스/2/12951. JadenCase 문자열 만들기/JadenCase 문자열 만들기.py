def solution(s):
    result = []
    a = True

    for char in s:
        if char == ' ':
            result.append(char)
            a = True
        elif a:
            result.append(char.upper())
            a = False
        else:
            result.append(char.lower())

    return ''.join(result)