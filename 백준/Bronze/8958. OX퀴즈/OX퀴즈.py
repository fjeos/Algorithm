for _ in range(int(input())):
    OX = list(input())
    weight, score = 0, 0
    for i in range(len(OX)):
        if OX[i] == 'O':
            weight += 1
        elif OX[i] == 'X':
            weight = 0
        score += weight
    print(score)