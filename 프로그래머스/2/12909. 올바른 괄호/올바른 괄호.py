def solution(s):
    left = 0
    right = 0
    for i in s:
        if i == '(':
            left += 1
        elif i == ')':
            right += 1
        if left < right:
            return False
    if left != right:
        return False
    else:
        return True 