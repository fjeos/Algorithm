def solution(n, arr1, arr2):
    answer = []
    
    for el in arr1:
        walls = bin(el).replace('0b', '')
        if len(walls) < n:
            walls = walls.zfill(n)
        answer.append(walls)

    for j in range(n):
        walls = bin(arr2[j]).replace('0b', '')
        if len(walls) < n:
            walls = walls.zfill(n)
            
        for k in range(n):
            if answer[j][k] != walls[k]:
                temp = list(answer[j])
                temp[k] = '1'
                answer[j] = ''.join(temp)
    for s in range(n):
        answer[s] = answer[s].replace('1', "#")
        answer[s] = answer[s].replace('0', " ")
    return answer