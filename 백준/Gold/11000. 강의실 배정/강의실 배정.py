import sys, heapq

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
subjects = sorted([list(map(int, input().split())) for _ in range(N)])
rooms = []
for subject in subjects:
    if rooms and rooms[0] <= subject[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, subject[1])
print(len(rooms))