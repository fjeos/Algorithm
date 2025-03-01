import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
channels = [input() for _ in range(N)]
answer = ''
i = 0
while channels[i] != "KBS1":
    i += 1
    answer += '1'
while i != 0:
    temp = channels[i]
    channels[i] = channels[i - 1]
    channels[i-1] = temp
    answer += '4'
    i -= 1
while channels[i] != "KBS2":
    i += 1
    answer += '1'
while i != 1:
    temp = channels[i]
    channels[i] = channels[i - 1]
    channels[i-1] = temp
    answer += '4'
    i -= 1
print(answer)