def solution(clothes):
    cnt = {}
    
    for i in clothes:
        item = i[1]
        if item in cnt:
            cnt[item] += 1
        else:
            cnt[item] = 1
    
    result = 1
    for v in cnt.values():
        result *= (v + 1)
    
    return result - 1
