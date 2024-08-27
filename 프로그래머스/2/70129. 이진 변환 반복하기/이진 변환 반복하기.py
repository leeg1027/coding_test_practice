def solution(s):
    cnt = 0
    count_0 = 0

    while True:
        cnt += 1
        count_0 += s.count('0')
        s = s.replace('0', '')
        a = len(s)
        new_s = []

        while a > 0:
            new_s.append(str(a % 2))
            a = a // 2

        new_s.reverse()
        s = "".join(new_s)

        if s == "1":
            break

    return [cnt, count_0]
