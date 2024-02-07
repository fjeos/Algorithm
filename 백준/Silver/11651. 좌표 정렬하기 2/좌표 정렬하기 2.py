import sys
input = sys.stdin.readline

points = [list(map(int, input().split())) for _ in range(int(input()))]
points.sort(key = lambda x:(x[1], x[0]))

for point in points:
    print(" ".join(map(str, point)))