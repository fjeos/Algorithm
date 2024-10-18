import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict
for _ in range(int(input())):
    N = int(input())
    teams = list(map(int, input().split()))
    dic_count = defaultdict(int)
    dic_score = defaultdict(list)

    rank = 1
    for i in range(N):
        if dic_count[teams[i]] == 0:
            dic_count[teams[i]] = teams.count(teams[i])
        if dic_count[teams[i]] == 6:
            dic_score[teams[i]].append(rank)
            rank += 1

    win_score = 1e9
    for score in dic_score.values():
        win_score = min(win_score, sum(score[:4]))

    win_teams = []
    for team in dic_score.values():
        if sum(team[:4]) == win_score:
            win_teams.append(team)

    win = 0
    for k in range(1):
        fifth = win_teams[k][4]
        for s in range(k + 1, len(win_teams)):
            if win_teams[s][4] < fifth:
                fifth = win_teams[s][4]
                win = s

    for key, value in dic_score.items():
        if value == win_teams[win]:
            print(key)