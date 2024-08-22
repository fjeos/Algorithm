import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
paper = list(map(int, input().split()))
result = [[] for _ in range(K + 1)]
def tree(buildings, depth):
    mid = len(buildings) // 2
    result[depth].append(buildings[mid])
    if len(buildings) == 1:
        return
    tree(buildings[:mid], depth + 1)
    tree(buildings[mid+1:], depth + 1)

    
tree(paper, 0)
for i in range(K):
    print(*result[i])