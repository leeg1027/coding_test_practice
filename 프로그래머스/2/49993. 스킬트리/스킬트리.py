def solution(skill, skill_trees):
    result = 0
    skill = list(skill)
    for i in range(len(skill_trees)):
        l = []
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                l.append(skill_trees[i][j])
        if skill[:len(l)] == l:
            result += 1
    return result