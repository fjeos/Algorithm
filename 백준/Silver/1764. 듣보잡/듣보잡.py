import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
dud = [input() for _ in range(N)]
bo = [input() for _ in range(M)]
result = list(set(dud) & set(bo))
print(len(result))
print('\n'.join(sorted(result)))