answer = []
def hanoi(n, from_pos, to_pos, temp_pos):
    if n == 1:
        answer.append([from_pos, to_pos])
        return
    #원반 n-1개를 temp_pos로 이동(보조기둥: to_pos)
    hanoi(n - 1, from_pos, temp_pos, to_pos)
    answer.append([from_pos, to_pos])
    #원반 n-1개를 to_pos로 이동(보조기둥: from_pos)
    hanoi(n - 1, temp_pos, to_pos, from_pos)
    
def solution(n):
    hanoi(n, 1, 3, 2)
    
    return answer