import sys
input = lambda: sys.stdin.readline()

N = int(input())
loss = list(map(int, input().split()))
loss.sort()
result = 0


def find_max_loss(start, end):
    global result
    while start < end:
        result = max(result, loss[end] + loss[start])
        start += 1
        end -= 1


# 운동 기구가 짝수개이면
if N % 2 == 0:
    find_max_loss(0, N - 1)

# 운동 기구가 홀수개이면
else:
    find_max_loss(0, N - 2)
    result = max(result, loss[-1])

print(result)
