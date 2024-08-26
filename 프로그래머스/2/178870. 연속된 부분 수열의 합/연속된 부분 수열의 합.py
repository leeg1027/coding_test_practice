def solution(sequence, k):
    start, end = 0, 0
    current_sum = 0
    min_length = float('inf')
    result = []

    while end < len(sequence):
        current_sum += sequence[end]
        
        while current_sum > k and start <= end:
            current_sum -= sequence[start]
            start += 1
        
        if current_sum == k:
            if (end - start + 1) < min_length:
                min_length = end - start + 1
                result = [start, end]
        
        end += 1
    
    return result