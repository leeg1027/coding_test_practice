def solution(n):
    cnt = 0
    for i in range(1, n+1):
        result = 0
        while 1:
            result += i
            i += 1
            if result == n:
                cnt += 1
            elif result > n:
                break
    return cnt