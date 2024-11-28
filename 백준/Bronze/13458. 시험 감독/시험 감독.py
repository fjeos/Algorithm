import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
rooms = list(map(int, input().split()))
chong, bu = map(int, input().split())

answer = 0
for room in rooms:
    answer += 1
    room = room - chong if room >= chong else 0
    answer += (room // bu)
    if room % bu != 0:
        answer += 1
print(answer)
