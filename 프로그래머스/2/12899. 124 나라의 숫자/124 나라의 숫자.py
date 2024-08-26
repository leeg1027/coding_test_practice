def solution(n):
    result = ''
    while 1:
        r = n % 3
        n = n // 3
        if r == 1:
            result += '1'
        elif r == 2:
            result += '2'
        elif r == 0:
            result += '4'
            n -= 1
        if (n == 0):
            break
    return result[::-1]
