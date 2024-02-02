import sys
input = sys.stdin.readline

N = int(input())
lists = [list(map(int, input().split())) for _ in range(N)]
lists.sort()

for i, j in lists:
    print(i, j)