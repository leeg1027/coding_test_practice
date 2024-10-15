def solution(priorities, location):
    a = len(priorities)
    result = 0
    cursor = 0
    while True:
        if max(priorities) == priorities[cursor%a]:
            priorities[cursor%a] = 0
            result += 1
            if cursor%a == location:
                break
        cursor += 1
    return result