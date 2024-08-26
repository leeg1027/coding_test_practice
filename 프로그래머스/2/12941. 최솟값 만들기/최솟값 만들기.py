def solution(A,B):
    result = 0
    A.sort()
    B.sort(reverse=True)
    for _ in range(len(A)):
        a = A.pop()
        b = B.pop()
        result += a*b
    return result