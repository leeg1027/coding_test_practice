def solution(clothes):
    cnt = {}
    
    # 의상 종류별로 몇 개 있는지 세기
    for i in clothes:
        item = i[1]
        if item in cnt:
            cnt[item] += 1
        else:
            cnt[item] = 1
    
    # 경우의 수 계산 (입지 않는 경우를 포함해서 +1)
    result = 1
    for v in cnt.values():
        result *= (v + 1)
    
    # 아무것도 입지 않는 경우 1을 제외
    return result - 1
