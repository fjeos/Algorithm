import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores.sort()
    count = N
    max_score2 = scores[0][1]
    for _, score2 in scores:
        if score2 > max_score2:
            count -= 1
        else:
            max_score2 = score2
    print(count)
