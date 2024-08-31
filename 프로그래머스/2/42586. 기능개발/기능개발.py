def solution(progresses, speeds):
    result = []
    a = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] == 0:
            a.append((100-progresses[i])//speeds[i])
        else:
            a.append((100-progresses[i])//speeds[i]+1)
            
    while a:
        cnt = 1
        days_to_deploy = a.pop(0) 
        while a and a[0] <= days_to_deploy:
            cnt += 1
            a.pop(0)
        
        result.append(cnt)
    
    return result