import sys
input = sys.stdin.readline

T = int(input())
lists = []
for _ in range(T):
    age, name = input().split()
    lists.append([int(age), name])

lists.sort(key = lambda x:x[0])
for i in lists:
    print(' '.join(map(str, i)))