import sys
input = sys.stdin.readline

N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]

if N > 1:
    tri[1][0] += tri[0][0]
    tri[1][1] += tri[0][0]

    for i in range(2, N):
        tri[i][0] += tri[i-1][0]
        tri[i][len(tri[i])-1] += tri[i-1][len(tri[i-1])-1]
        for j in range(1, len(tri[i])-1):
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
print(max(tri[N-1]))