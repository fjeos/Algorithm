import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
boards = [list(input()) for _ in range(N)]
W_boards = ['WBWBWBWB', 'BWBWBWBW'] * 4
B_boards = ['BWBWBWBW', 'WBWBWBWB'] * 4


def check_boards(arr):
    w_count, b_count = 0, 0
    for k in range(8):
        for s in range(8):
            if arr[k][s] != W_boards[k][s]:
                w_count += 1
            if arr[k][s] != B_boards[k][s]:
                b_count += 1
    return min(w_count, b_count)


min_value = sys.maxsize
for i in range(N - 7):
    for j in range(M - 7):
        min_value = min(min_value, check_boards([row[j:j + 8] for row in boards[i:i + 8]]))

print(min_value)
