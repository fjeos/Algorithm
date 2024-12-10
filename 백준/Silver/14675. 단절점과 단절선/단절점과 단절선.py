import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

for _ in range(int(input())):
    t, k = map(int, input().split())
    if t == 1:
        print("yes") if len(tree[k]) > 1 else print("no")
    else:
        print("yes")