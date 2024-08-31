def solution(n, words):
    result = []
    past_word = [words[0]]
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            return [(i%n)+1, (i//n)+1]
        elif words[i] in past_word:
            return [(i%n)+1, (i//n)+1]
        else:
            past_word.append(words[i])
    else:
        return [0, 0]