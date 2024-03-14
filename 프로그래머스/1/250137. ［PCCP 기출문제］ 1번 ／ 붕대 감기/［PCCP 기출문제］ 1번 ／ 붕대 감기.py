def solution(bandage, health, attacks):
    answer = health
    last_time = attacks[-1][0]
    continuous = 0
    i = 0
    attack_time = attacks[i][0]
    for time in range(last_time+1):
        if attack_time == time:
            answer -= attacks[i][1]
            if answer <= 0:
                answer = -1
                break
            continuous = 0
            i += 1
            if i == len(attacks): break
            attack_time = attacks[i][0]

        else:
            answer += bandage[1]
            continuous += 1
            if continuous == bandage[0]:
                answer += bandage[2]
                continuous = 0
            if answer > health:
                answer = health
    return answer