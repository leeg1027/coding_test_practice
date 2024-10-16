def solution(word):
    result = 0
    alpha  = ["A","E","I","O","U",""]
    ans = []
    for i in alpha:
        for j in alpha:
            for k in alpha:
                for l in alpha:
                    for m in alpha:
                        w = i+j+k+l+m
                        if w not in ans: ans.append(w)
    ans.sort()
    result = ans.index(word)
    return result