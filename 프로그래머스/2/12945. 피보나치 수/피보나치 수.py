def solution(n):
    result = 0
    a = 0
    b = 1
    for _ in range(n-1):
        result = a + b
        a = b
        b = result
    return result%1234567