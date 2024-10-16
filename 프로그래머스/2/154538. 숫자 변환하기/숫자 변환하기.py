from collections import deque

def solution(x, y, n):
    
    que = deque([(x, 0)])
    visited = [False] * (y + 1)

    while que:
        current, steps = que.popleft()
        
        if current == y:
            return steps
        
        next_numbers = [current + n, current * 2, current * 3]
        
        for next_num in next_numbers:
            if next_num <= y and not visited[next_num]:
                visited[next_num] = True
                que.append((next_num, steps + 1))
    
    return -1