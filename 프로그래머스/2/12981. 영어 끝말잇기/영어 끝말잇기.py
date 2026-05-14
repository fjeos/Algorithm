import math
def solution(n, words):
    answer = []
    word = {words[0]}
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in word:
            return [i % n + 1, math.ceil(i//n) + 1]
        word.add(words[i])
            

    return [0, 0]