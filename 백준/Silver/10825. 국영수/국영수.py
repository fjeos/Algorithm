import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
score = [[] for _ in range(N)]
for i in range(N):
    student = input().split()
    score[i].append(student[0])
    score[i].append(list(map(int, student[1:])))
score.sort(key = lambda x:(-x[1][0], x[1][1], -x[1][2], x[0]))
for name in score:
    print(name[0])