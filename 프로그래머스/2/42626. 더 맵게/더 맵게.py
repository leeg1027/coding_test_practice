import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    while len(scoville) >= 2:
        first = heapq.heappop(scoville)
        if first >= K:
            return cnt
        
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        cnt += 1
    
    if len(scoville) == 1 and scoville[0] >= K:
        return cnt
    
    return -1
