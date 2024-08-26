def solution(s):
    result = ''
    s_split = list(map(int, s.split()))
    result += str(min(s_split)) + ' ' + str(max(s_split))
    return result