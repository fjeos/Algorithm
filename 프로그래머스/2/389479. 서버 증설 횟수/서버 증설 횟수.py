from collections import deque
def solution(players, m, k):
    answer = 0
    servers = deque()
    now_servers, n = 0, 0
    for player in players:
        for i in range(len(servers)):
            servers[i][1] += 1
        while servers and servers[0][1] == k:
            servers.popleft()
        if player < m:
            continue
        if len(servers) * m <= player:
            n = player // m
            if n <= len(servers):
                continue
            answer += n - len(servers)
            while len(servers) < n:
                servers.append([0, 0])
    return answer
