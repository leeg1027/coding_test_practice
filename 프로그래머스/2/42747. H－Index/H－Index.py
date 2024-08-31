def solution(citations):
    for i in range(max(citations), 0, -1):
        cnt = 0
        for n in citations:
            if n >= i:
                cnt += 1.
        if cnt >= i:
            return i
    return 0