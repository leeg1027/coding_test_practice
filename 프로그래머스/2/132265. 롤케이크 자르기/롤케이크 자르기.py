def solution(topping):
    result = 0
    
    left_set = set()
    left_unique = []
    for t in topping:
        left_set.add(t)
        left_unique.append(len(left_set))
    
    right_set = set()
    right_unique = []
    for t in reversed(topping):
        right_set.add(t)
        right_unique.append(len(right_set))
    right_unique.reverse()
    
    for i in range(len(topping) - 1):
        if left_unique[i] == right_unique[i + 1]:
            result += 1
    
    return result
