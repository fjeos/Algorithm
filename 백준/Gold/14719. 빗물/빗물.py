import sys

input = lambda: sys.stdin.readline().rstrip()

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

count = 0
for i in range(H):
    start_block = -1
    for j in range(W):
        if blocks[j] > i:
            if start_block != -1:
                count += j - start_block - 1
            start_block = j

print(count)
