import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
switch = list(map(int, input().split()))
for _ in range(int(input())):
    gen, num = map(int, input().split())
    if gen == 1:
        index = num - 1
        while index < N:
            switch[index] = 1 if switch[index] == 0 else 0
            index += num
    else:
        center = num - 1
        switch[center] = 1 if switch[center] == 0 else 0
        for i in range(1, N // 2):
            start, end = center - i, center + i
            if start > -1 and end < N and switch[start] == switch[end]:
                switch[start] = 1 if switch[start] == 0 else 0
                switch[end] = 1 if switch[end] == 0 else 0
            else:
                break
count = 0
for i in range(N):
    print(switch[i], end=' ')
    count += 1
    if count == 20:
        print()
        count = 0

