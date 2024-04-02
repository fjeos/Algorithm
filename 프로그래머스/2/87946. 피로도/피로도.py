def solution(k, dungeons):
    dungeon = []
    for i in permutations(dungeons, len(dungeons)):
        dungeon.append(list(i))

    answer = []
    for i in range(len(dungeon)):
        pirodo = k
        count = 0
        for j in dungeon[i]:
            if pirodo >= j[0]:
                pirodo -= j[1]
                count += 1
            else:
                break
        answer.append(count)     
    return max(answer)

from itertools import permutations