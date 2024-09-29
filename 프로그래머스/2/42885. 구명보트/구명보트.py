def solution(people, limit):
    people.sort(reverse=True)
    l, r = 0, len(people) - 1
    result = 0
    
    while l <= r:
        if people[l] + people[r] <= limit:
            r -= 1
        l += 1
        
        result += 1
    
    return result