def solution(order):
    storage = order.copy()
    storage.sort()
    sub = []
    answer = 0
    idx = 0
    
    for i in order:
        while idx < len(storage) and storage[idx] <= i:
            sub.append(storage[idx])
            idx += 1
        
        if sub and sub[-1] == i:
            sub.pop()
            answer += 1
        else:
            break
    
    return answer