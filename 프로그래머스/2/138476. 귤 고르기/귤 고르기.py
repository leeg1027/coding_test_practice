from collections import Counter
def solution(k, tangerine):
    result = 0
    cnt = Counter(tangerine)
    sorted_cnt = sorted(cnt.values(), reverse=True)
    
    j = 0
    while k > 0:
        k -= sorted_cnt[j]
        result += 1
        j += 1
    return result