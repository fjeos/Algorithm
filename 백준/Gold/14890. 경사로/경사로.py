import sys
input = lambda: sys.stdin.readline().rstrip()

N, L = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
count = 0


def check_line(line):
    visited = [False for _ in range(N)]
    for i in range(1, N):
        # 낮은 칸과 높은 칸의 높이 차이가 1이 아님
        if abs(line[i - 1] - line[i]) > 1:
            return False
        else:
            if line[i - 1] - line[i] == 1:
                for j in range(L):
                    if i + j >= N or line[i] != line[i + j] or visited[i + j]:
                        return False
                    if not visited[i + j]:
                        visited[i + j] = True
            elif line[i] - line[i - 1] == 1:
                for j in range(L):
                    if i - 1 - j < 0 or line[i - 1] != line[i - 1 - j] or visited[i - 1 - j]:
                        return False
                    if not visited[i - 1 - j]:
                        visited[i - 1 - j] = True

    return True


for k in range(N):
    if check_line(road[k]):
        count += 1
for n in range(N):
    if check_line([road[s][n] for s in range(N)]):
        count += 1

print(count)
