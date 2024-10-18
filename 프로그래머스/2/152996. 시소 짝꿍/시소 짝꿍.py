from collections import defaultdict

def solution(weights):
    answer = 0
    weight_count = defaultdict(int)
    
    for weight in weights:
        weight_count[weight] += 1
    
    for weight in weights:
        answer += weight_count[weight] - 1
        
        for ratio in [(2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3)]:
            scaled_weight = weight * ratio[0] // ratio[1]
            if weight * ratio[0] % ratio[1] == 0 and scaled_weight in weight_count:
                answer += weight_count[scaled_weight]
    
    return answer // 2
