def solution(n, computers):
    answer = 0

    queue = []
    visited = []

    for com in range(n):
        if com not in visited:
            queue.append(com)
            answer += 1

            while queue:
                now = queue.pop(0)    
                for i in range(n):
                    if computers[now][i] == 1 and i not in visited:
                        visited.append(i)
                        queue.append(i)
    return answer