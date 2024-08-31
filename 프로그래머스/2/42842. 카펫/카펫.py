def solution(brown, yellow):
    for i in range(1, yellow+1):
        row = i
        col = yellow//i
        if brown == ((col+2)*2 + row*2) and yellow == col*row:
            result = [col+2, row+2]
            return result